from dijkstra.dijkstra import dijkstra
from utils.utils import read_to_graph

graph = read_to_graph(file_name="paths.geojson")
distance, shortest_path = dijkstra(graph=graph, initial="n189", end="n167")

if shortest_path:
    graph.nodes_to_csv(file_name="shortest_path.csv", path=shortest_path)

    print(f"{distance}m", f"From {shortest_path[0]} To {shortest_path[-1]}")

else:
    print("RouteNotPossible")
