import shapefile as sp
from dbfread import DBF

''' To access data download two files from iris_geo directory on Google Storage

    * Use get_box_coord(iris_id) to get two points of iris to obtain a box
    * Use get_poly_coord(iris_id) to get a polygone to obtain exact borders of an iris

    - To get the correspondance of iris_id and iris_type use get_iris_type('iris_id')
'''

class Iris():
    def __init__(self):
        self.get_files()
        self.get_records()
        self.get_iris_id()

    def get_files(self):
        path_dbf = '../raw_data/iris_geo/IRIS_GEO_2018_FRTOT.dbf'
        path_shp = '../raw_data/iris_geo/IRIS_GEO_2018_FRTOT.shp'

        self.dbf = DBF(path_dbf)
        self.shp = sp.Reader(path_shp)

    def get_records(self):
        records = []
        for record in self.dbf:
            records.append(dict(record))
        self.records = records

    def get_iris_id(self):
        iris_id = []
        for i in range(len(self.records)):
            r = self.records[i]['CODE_IRIS']
            iris_id.append(r)
        self.iris_id = iris_id
    def get_iris_type(self, iris_id):
        iris_type = {}
        for i in range(len(self.records)):
            iris_type[self.iris_id[i]]= self.records[i]['TYP_IRIS']
        self.iris_type = iris_type
        return iris_type[str(iris_id)]

    def get_iris_type(self):
        iris_id = []
        for i in range(len(self.records)):
            r = self.records[i]['TYP_IRIS']
            iris_id.append(r)
        self.iris_id = iris_id

    def get_box_coord(self, iris_id):
        shapes = self.shp.shapes()
        box_coord = {}
        for i in range(len(shapes)):
            box_coord[self.iris_id[i]] = shapes[i].bbox
        return box_coord[str(iris_id)]

    def get_poly_coord(self, iris_id):
        shapes = self.shp.shapes()
        poly_coord = {}
        for i in range(len(shapes)):
            poly_coord[self.iris_id[i]] = shapes[i].__geo_interface__[
                'coordinates'][0]
        return poly_coord[str(iris_id)]
