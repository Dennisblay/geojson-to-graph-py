from collections import defaultdict
from node import Node


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
        self.nodes = {}
        self.weights = {}

    def add_node(self, from_node: Node, to_node: Node, weight):
        # Note: assumes edges are bi-directional

        self.nodes[from_node.label] = (from_node.x, from_node.y, from_node.label)
        self.nodes[to_node.label] = (to_node.x, to_node.y, to_node.label)
        self.edges[from_node.label].append(to_node.label)
        self.edges[to_node.label].append(from_node.label)
        self.weights[f"{from_node.label}-{to_node.label}"] = weight
        self.weights[f"{to_node.label}-{from_node.label}"] = weight
