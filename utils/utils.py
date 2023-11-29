import hashlib
import math
from graph.graph import Node


def generate_unique_key(data):
    data_bytes = bytes(str(data), 'utf-8')

    hash_object = hashlib.md5(data_bytes)

    unique_key = hash_object.hexdigest()

    return unique_key


def get_weight(from_node: Node, to_node: Node) -> float:
    # Euclidean distance
    delta_y = to_node.y - from_node.y
    delta_x = to_node.x - from_node.x
    distance = math.sqrt((delta_y ** 2 + delta_x ** 2))
    return distance


def is_adjacent(previous, current) -> bool:
    return previous[-1] == current[0]
