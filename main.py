from dijkstra.dijkstra import dijkstra
from utils.utils import read_to_graph

graph = read_to_graph(file_name="paths.geojson")
distance, shortest_path = dijkstra(graph=graph, initial="n189", end="n167")

if shortest_path:
    graph.nodes_to_csv()

    print(f"{distance}m", f"From {shortest_path[0]} To {shortest_path[-1]}")

else:
    print("RouteNotPossible")

"""
Point (-1.56487150913662632 6.67332465855798684)
"""
# point = Point (-1.56487150913662632,  6.67332465855798684)
query = graph.query_closest_location(x=-175195.91816760387632, y=745551.944510839, label="park_point")
print(query)
