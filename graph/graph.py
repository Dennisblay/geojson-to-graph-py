from collections import defaultdict
import math


class Node(object):

    def __init__(self, point_id=None, label=None, x=None, y=None):
        self.point_id = point_id
        self.label = label
        self.x = x
        self.y = y


def get_weight(from_node: Node, to_node: Node) -> float:
    # Euclidean distance
    delta_y = to_node.y - from_node.y
    delta_x = to_node.x - from_node.x
    distance = math.sqrt((delta_y ** 2 + delta_x ** 2))
    return distance


def is_adjacent(previous, current) -> bool:
    return previous[-1] == current[0]


class Graph(object):

    def __init__(self):
        """
               self.edges is a dict of all possible next nodes
               e.g. {'X': ['A', 'B', 'C', 'E'], ...}
               self.weights has all the weights between two nodes,
               with the two nodes as a tuple as the key
               e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
               """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_node(self, from_node: Node, to_node: Node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node.label].append(to_node.label)
        self.edges[to_node.label].append(from_node.label)
        self.weights[(from_node.label, to_node.label)] = weight
        self.weights[(to_node.label, from_node.label)] = weight
