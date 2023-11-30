import math
from shapely.geometry import LineString
import geopandas as gdp
from graph.graph import Node, Graph


class NodeKeyGenerator:

    def __init__(self):
        self.counter = 1
        self.key_map = {}

    def generate_node_key(self, data):
        if data in self.key_map:
            return self.key_map[data]

        key = f"n{self.counter}"
        self.counter += 1
        self.key_map[data] = key
        return key


# Usage


def is_adjacent(previous, current) -> bool:
    if previous is not None:
        return previous.coords[-1] == current.coords[0]


def read_to_graph(file_name):
    new_graph = Graph()
    node_key_generator = NodeKeyGenerator()

    gdf = gdp.read_file(file_name)

    for index, current_row in gdf.iterrows():

        densified_segment = list(densify_segment(current_row=current_row, distance=2).coords)

        if len(densified_segment) != 0:

            prev_coords_pair = None
            for (x, y) in densified_segment:
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

                    new_graph.add_node(from_node=from_node, to_node=to_node,
                                       weight=new_graph.get_weight(from_node=from_node,
                                                                   to_node=to_node))
                prev_coords_pair = x, y

    return new_graph


def densify_segment(current_row, distance=2):
    current_segment = current_row.geometry
    length_of_segment = current_segment.length
    points = [current_segment.interpolate(i) for i in range(distance, math.floor(length_of_segment), distance)]
    return LineString(list(current_segment.coords) + [(point.x, point.y) for point in points])
