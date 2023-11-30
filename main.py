from dijkstra.dijkstra import dijkstra
from utils.utils import read_to_graph

graph = read_to_graph(file_name="paths.geojson")
distance, shortest_path = dijkstra(graph=graph, initial="n189", end="n167")

if shortest_path:
    graph.nodes_to_csv()

    print(f"{distance}m", f"From {shortest_path[0]} To {shortest_path[-1]}")

else:
    print("RouteNotPossible")

distance, closest_node = graph.query_closest_location(x=-175195.91816760387632, y=745551.944510839, label="park_point")
graph.node_to_csv(closest_node)
