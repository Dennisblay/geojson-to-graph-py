from dijkstra.dijkstra import dijkstra
from utils.utils import reader
from pprint import pprint

graph = reader(file_name="paths.geojson")
distance, shortest_path = dijkstra(graph=graph, initial="n1", end="n4")

graph.nodes_to_csv(file_name="shortest_path.csv", path=shortest_path)
print(distance)
