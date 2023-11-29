import geopandas as gdp
from graph.graph import Graph, Node, get_weight, is_adjacent
from pprint import pprint

gdf = gdp.read_file("paths_test.geojson")

new_graph = Graph()
prev_multi_line = None
for index, current_row in gdf.iterrows():
    for multi_line in current_row.geometry.geoms:
        print(list(multi_line.coords))
        curr_coords = list(multi_line.coords)

        from_node = Node(
            x=curr_coords[0][0],
            y=curr_coords[0][1]
        )

        to_node = Node(
            x=curr_coords[1][0],
            y=curr_coords[1][1]
        )

        new_graph.add_node(from_node=from_node, to_node=to_node,
                           weight=get_weight(from_node=from_node,
                                             to_node=to_node))

pprint(new_graph.edges)
pprint(new_graph.weights)
