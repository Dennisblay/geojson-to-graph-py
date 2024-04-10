from dijkstra.dijkstra import dijkstra
from utils.utils import read_to_graph
import os
from pprint import pprint

if os.path.exists(path="paths.geojson"):
    graph = read_to_graph(file_name="paths.geojson", should_densify_segments=True, distance=2)

    """
P1   (X,Y) -174320.829365919722477, 744498.63213670917321
    """


    # distance_from_query_point, closest_node = graph.query_closest_location(x=-174320.829365919722477,
    #                                                                        y=744498.63213670917321,
    #                                                                        label="P1")
    # graph.node_to_csv(closest_node)  # Save to CSV for visualization

    distance, shortest_path = dijkstra(graph=graph, initial='n1',
                                        end="n10")   

    if shortest_path:
    	graph.nodes_to_csv(paths=shortest_path, file_name="text_janice.csv")
    	graph.nodes_to_csv()
  
    	print(f"{distance}m", f"From {shortest_path[0]} To {shortest_path[-1]}")

    else:
        print("RouteNotPossible")

else:
     print("File does not exist, Check file path integrity")
     pprint(graph.nodes)
   
