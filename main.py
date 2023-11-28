import geopandas as gdp

gdf = gdp.read_file("paths.geojson")


print(gdf.head().geometry)

