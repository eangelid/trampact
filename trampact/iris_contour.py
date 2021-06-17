import pandas as pd
import numpy as np
import geopandas as gpd
import ipyleaflet
from ipyleaflet import Map, GeoData, basemaps, LayersControl, Polyline, LegendControl, LayersControl
import json
import branca.colormap as cm
from branca.colormap import linear
'''To plot a colored map of iris by a feature provide:
    - a csvfile_path to df
    - a feature from df
    Note that df must contain an 'iris_id' column
'''
csvfile_path = "gs://trampact_storage/data/g_p_2006_2016_Nice.csv"
#"../raw_data/data_BD_GENT_2006.csv"
feature = 'TE_HH_2voit'
#"t_actifs_2006"

center = (43.723348, 7.285484)
zoom = 10


class Contour():
    def __init__(self):
        self.feature = feature
        self.get_files(csvfile_path)
        self.get_geo_data(city_of_nice=False)
        self.get_features_data(self.feature)
        self.get_lines()
        #self.plot_map(center=center, zoom=zoom)

    def get_files(self, csvfile_path):
        '''Read data from files:
              - your feature-df
              - geo data
              - tramway line data'''
        zipfile = "../raw_data/iris_geo/iris-geo-2018-frtot.zip"
        csv_t1_path = "gs://trampact_storage/data/coord_T1.csv"
        csv_t2_path = "gs://trampact_storage/data/lignt_t2_coord.csv"

        self.csv_t1 = pd.read_csv(csv_t1_path)
        self.csv_t2 = pd.read_csv(csv_t2_path)
        self.csv = pd.read_csv(csvfile_path)
        self.csv.iris_id = self.csv.iris_id.map(lambda x: str(0) + str(x))
        self.data = gpd.read_file(zipfile)


    def set_is_city_of_nice(self, city_of_nice=False):
        self.get_geo_data(city_of_nice)
        self.get_features_data(self.feature)

    def get_geo_data(self, city_of_nice=False):
        '''Read and filter geo data at a departement level by default
           To filter at a city level, set boolean to True
        '''
        if not city_of_nice:
            mask = self.data[[
                'CODE_IRIS'
            ]].apply(lambda x: x.str.startswith('06')).any(axis=1)
            self.city_of_nice = False
        else:
            mask = self.data['NOM_COM'] == 'Nice'
            self.city_of_nice = True
        self.gdf = self.data[mask]
        self.gdf_json = self.gdf.to_json()
        dict_json = json.loads(self.gdf_json)
        for feature in dict_json['features']:
            feature['id'] = feature['properties']['CODE_IRIS']
        self.dict_json = dict_json

    def get_features_data(self, feature):
        '''Set feature data to dictionary format
           Set length accoring to geo level
        '''
        #import ipdb; ipdb.set_trace()
        self.feature_dict = dict(
            zip(self.csv['iris_id'].tolist(), self.csv[feature].tolist()))
        if self.city_of_nice == False:
            self.feature_dict = self.feature_dict
        else:
            nce_filter = self.gdf['CODE_IRIS'].to_list()
            nce_feature_dict = {}
            for (k, v) in self.feature_dict.items():
                if k in nce_filter:
                    nce_feature_dict[k] = v
            self.feature_dict = nce_feature_dict

    def get_lines(self):
        '''Get points for tramway lines'''
        points_t1 = []
        for i in range(len(self.csv_t1)):
            t = [self.csv_t1.loc[i, 'y'], self.csv_t1.loc[i, 'x']]
            points_t1.append(t)
        self.points_t1 = points_t1
        points_t2 = []
        for i in range(len(self.csv_t2)):
            t = [self.csv_t2.loc[i, 'lat'], self.csv_t2.loc[i, 'lon']]
            points_t2.append(t)
        self.points_t2 = points_t2

    def plot_map(self, center=center, zoom=zoom):
        colormap = cm.LinearColormap(
            cm.linear.YlOrRd_04.colors,
            vmin=np.min(list(self.feature_dict.values())),
            vmax=np.max(list(self.feature_dict.values())))

        line1 = Polyline(name='Ligne 1',
                         locations=self.points_t1,
                         style={
                             'color': 'red',
                             'fillColor': 'red',
                             'opacity': 0.5,
                             'weight': 9,
                             'dashArray': '2',
                             'fillOpacity': 0.6
                         },
                         fill=False)

        '''line2 = Polyline(name='Ligne 2',
                         locations=self.points_t2,
                         style={
                             'color': 'blue',
                             'fillColor': '#3366cc',
                             'opacity': 0.5,
                             'weight': 9,
                             'dashArray': '2',
                             'fillOpacity': 0.8
                         },
                         fill=False)'''

        layer = ipyleaflet.Choropleth(geo_data=self.dict_json,
                                      choro_data=self.feature_dict,
                                      colormap=colormap,
                                      border_color='gray',
                                      style={
                                          'fillOpacity': 0.90,
                                          'dashArray': '2, 2'
                                      })

        legend = LegendControl(
            {
               'low': #str(np.min(list(self.feature_dict.values())))
                colormap.rgb_hex_str(np.min(list(self.feature_dict.values()))),
                "medium":
                colormap.rgb_hex_str(np.mean(list(
                    self.feature_dict.values()))),
                "high":
                colormap.rgb_hex_str(np.max(list(self.feature_dict.values())))
            },
            name=self.feature,
            position="bottomright")

        m = ipyleaflet.Map(center=center, zoom=zoom)
        m.add_control(legend)
        m.add_layer(layer)
        m.add_layer(line1)
        #m.add_layer(line2)

        control = LayersControl(position='topright')
        m.add_control(LayersControl())

        return m
