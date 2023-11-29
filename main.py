import geopandas as gdp
from dijkstra.dijkstra import dijkstra
from graph.graph import Graph
from graph.Node import Node, NodeContainer
from utils.utils import get_weight, is_adjacent, NodeKeyGenerator
from pprint import pprint

gdf = gdp.read_file("paths.geojson")

new_graph = Graph()
new_node_container = NodeContainer()
prev_coords_pair = None
node_key_generator = NodeKeyGenerator()
for index, current_row in gdf.iterrows():
    current_segment = list(current_row.geometry.coords)
    if len(current_segment) != 0:
        for (x, y) in current_segment:
            if prev_coords_pair is not None:
                from_node = Node(
                    x=x,
                    y=y,
                    label=node_key_generator.generate_node_key(f"{x}-{y}")
                )

                x_to, y_to = prev_coords_pair
                to_node = Node(
                    x=x_to,
                    y=y_to,
                    label=node_key_generator.generate_node_key(f"{x_to}-{y_to}")
                )

                # new_node_container.add_node()
                new_graph.add_node(from_node=from_node, to_node=to_node,
                                   weight=get_weight(from_node=from_node,
                                                     to_node=to_node))
            prev_coords_pair = x, y
pprint(new_graph.edges)
pprint(new_graph.weights)

print(dijkstra(graph=new_graph, initial="n1", end="n20"))
