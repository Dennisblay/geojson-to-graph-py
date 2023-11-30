from collections import defaultdict
from utils.utils import get_weight
import csv


class Node(object):

    def __init__(self, point_id=None, label=None, x=None, y=None):
        self.point_id = point_id
        self.label = label
        self.x = x
        self.y = y


class Graph(object):
    TOLERANCE = 30e-2

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

    def nodes_to_csv(self, file_name="shortest_path.csv", path=None):
        all_nodes = [self.nodes[node] for node in self.nodes]
        if path is not None:
            all_nodes = [self.nodes[node] for node in path]

        headers = ['X', 'Y', 'L']
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(all_nodes)

    def dissolve_close_nodes(self):
        for node in self.nodes:
            for node_to_compare in self.nodes:
                if get_weight(node, node_to_compare) < self.TOLERANCE:
                    pass
        pass
