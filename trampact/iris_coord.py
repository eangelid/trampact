import shapefile as sp
from dbfread import DBF

''' ! Please download two files from gs://data/iris_geo in order to use the package
    ! iris_id has 9 digits
'''

class Iris():
    def __init__(self):
        self.get_files()
        self.get_records()
        self.get_iris_id()

    def get_files(self):
        '''Read data from locally saved files'''
        path_dbf = '../raw_data/iris_geo/IRIS_GEO_2018_FRTOT.dbf'
        path_shp = '../raw_data/iris_geo/IRIS_GEO_2018_FRTOT.shp'

        self.dbf = DBF(path_dbf)
        self.shp = sp.Reader(path_shp)

    def get_records(self):
        '''Get a list of dictionaries with coordinates data'''
        records = []
        for record in self.dbf:
            records.append(dict(record))
        self.records = records

    def get_iris_id(self):
        '''Create a list of all iris_ids of France'''

        iris_id = []
        for i in range(len(self.records)):
            r = self.records[i]['CODE_IRIS']
            iris_id.append(r)
        self.iris_id = iris_id

    def get_iris_type(self, iris_id):
        '''Get the type of iris (H, A, Z) given iris_id'''

        iris_type = {}
        for i in range(len(self.records)):
            iris_type[self.iris_id[i]]= self.records[i]['TYP_IRIS']
        self.iris_type = iris_type
        return iris_type[str(iris_id)]

    def get_box_coord(self, iris_id):
        '''Get approximative iris coordinates in a rectangular form'''

        shapes = self.shp.shapes()
        box_coord = {}
        for i in range(len(shapes)):
            box_coord[self.iris_id[i]] = shapes[i].bbox
        return box_coord[str(iris_id)]

    def get_poly_coord(self, iris_id):
        '''Get exact iris coordinates in a polynomial form'''
        shapes = self.shp.shapes()
        poly_coord = {}
        for i in range(len(shapes)):
            poly_coord[self.iris_id[i]] = shapes[i].__geo_interface__[
                'coordinates'][0]
        return poly_coord[str(iris_id)]

    def get_iris_list(self):
        '''Get the list of all iris_ids of France'''
        iris_id = []
        for i in range(len(records)):
            r = records[i]['CODE_IRIS']
            iris_id.append(r)
        return iris_id
