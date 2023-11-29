import math
from graph.graph import Node


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


def get_weight(from_node: Node, to_node: Node) -> float:
    # Euclidean distance
    delta_y = to_node.y - from_node.y
    delta_x = to_node.x - from_node.x
    return math.sqrt((delta_y ** 2 + delta_x ** 2))


def is_adjacent(previous, current) -> bool:
    if previous is not None:
        return previous.coords[-1] == current.coords[0]
