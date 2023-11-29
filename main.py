import geopandas as gdp
from graph.graph import Graph, Node
from utils.utils import get_weight, is_adjacent, NodeKeyGenerator
from pprint import pprint

gdf = gdp.read_file("paths_test.geojson")

new_graph = Graph()
prev_multi_line = None
node_key_generator = NodeKeyGenerator()
for index, current_row in gdf.iterrows():
    for multi_line in current_row.geometry.geoms:
        print(list(multi_line.coords))
        curr_coords = list(multi_line.coords)
        x_from = curr_coords[0][0]  # X1
        y_from = curr_coords[0][1]  # Y1

        x_to = curr_coords[1][0]  # X2
        y_to = curr_coords[1][1]  # Y2

        from_node = Node(
            x=x_from,
            y=y_from,
            label=node_key_generator.generate_node_key(f"{x_from}-{y_from}")
        )

        to_node = Node(
            x=x_to,
            y=y_to,
            label=node_key_generator.generate_node_key(f"{x_to}-{y_to}")
        )

        new_graph.add_node(from_node=from_node, to_node=to_node,
                           weight=get_weight(from_node=from_node,
                                             to_node=to_node))
pprint(new_graph.edges)
pprint(new_graph.weights)
