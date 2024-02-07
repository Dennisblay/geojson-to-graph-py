import geopandas as gdp
from pprint import pprint

buildings = gdp.read_file('/home/denis/Documents/buildings_v1.shp')

buildings.to_csv('results.csv')