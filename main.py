from dijkstra.dijkstra import dijkstra
from utils.utils import read_to_graph
import os

if os.path.exists(path="paths.geojson"):

    graph = read_to_graph(file_name="paths.geojson")
    distance, shortest_path = dijkstra(graph=graph, initial="n189", end="n167")

    if shortest_path:
        graph.nodes_to_csv()

        print(f"{distance}m", f"From {shortest_path[0]} To {shortest_path[-1]}")

    else:
        print("RouteNotPossible")

    distance, closest_node = graph.query_closest_location(x=-174200.003671526181279, y=744552.949123957310803,
                                                          label="park_point")
    graph.node_to_csv(closest_node)

else:
    print("File does not exist, Check file path integrity")
