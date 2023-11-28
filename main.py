import geopandas as gdp
from graph.graph import Graph, Node, get_weight, is_adjacent
from pprint import pprint

gdf = gdp.read_file("paths.geojson")

new_graph = Graph()
prev_row = None
for index, current_row in gdf.iterrows():
    if prev_row is not None:
        curr_coords = list(current_row.geometry.coords)
        prev_coords = list(prev_row.geometry.coords)

        from_node = Node(
            point_id=prev_row.id,
            name=prev_row.Location,
            x=prev_coords[0][0],
            y=prev_coords[0][1]
        )

        to_node = Node(
            point_id=current_row.id,
            name=current_row.Location,
            x=curr_coords[0][0],
            y=curr_coords[0][1]
        )

        new_graph.add_node(from_node=from_node, to_node=to_node,
                           weight=get_weight(from_node=from_node,
                                             to_node=to_node),
                           are_neighbors=is_adjacent(prev_coords, curr_coords))
    prev_row = current_row

print(new_graph.edges)
print(new_graph.weights)
