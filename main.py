import csv
from dijkstra.dijkstra import dijkstra
from utils.utils import NodeKeyGenerator, reader
from pprint import pprint

node_key_generator = NodeKeyGenerator()
graph = reader(file_name="paths.geojson")
# pprint(graph.nodes)
# pprint(graph.edges)
# pprint(graph.weights)
shortest_path = dijkstra(graph=graph, initial="n265", end="n97")

graph.nodes_to_csv(file_name="shortest_path.csv", path=shortest_path)
