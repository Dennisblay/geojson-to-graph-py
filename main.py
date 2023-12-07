from dijkstra.dijkstra import dijkstra
from utils.utils import read_to_graph
import os
from pprint import pprint

if os.path.exists(path="paths.geojson"):
    graph = read_to_graph(file_name="paths.geojson", should_densify_segments=True, distance=2)
    pprint(graph.edges["n2442"])

    """
P1   (X,Y) -174330.937208184128394, 744500.627697278396226
P2   (X,Y) -174245.345261112553999, 744662.047880616504699
    """

    distance_from_query_point, closest_node = graph.query_closest_location(x=-174330.937208184128394,
                                                                           y=744500.627697278396226174200,
                                                                           label="P1")
    graph.node_to_csv(closest_node)  # Save to CSV for visualization

    distance, shortest_path = dijkstra(graph=graph, initial="n2442",
                                       end="n2103")  # From Query Location to N-Block(Node 624)

    if shortest_path:
        # pprint(shortest_path)
        graph.nodes_to_csv(paths=shortest_path, file_name="New.csv")
        # graph.nodes_to_csv()

        print(f"{distance}m", f"From {shortest_path[0]} To {shortest_path[-1]}")

    else:
        print("RouteNotPossible")

else:
    print("File does not exist, Check file path integrity")
