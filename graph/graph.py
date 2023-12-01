from collections import defaultdict
import math
import csv


class Node(object):

    def __init__(self, point_id=None, label=None, x=None, y=None):
        self.point_id = point_id
        self.label = label
        self.x = x
        self.y = y


class Graph(object):

    def __init__(self):
        """
               self.edges is a dict of all possible next nodes
               e.g. {'X': { 'A', 'B', 'C', 'E' }, ...}
               self.weights has all the weights between two nodes,
               with the two nodes as a tuple as the key
               e.g. {('X-A'): 7, ('A-X'): 2, ...}
               """
        self.edges = defaultdict(set)
        self.nodes = {}
        self.weights = {}

    def add_node(self, from_node: Node, to_node: Node, weight):
        # Note: assumes edges are bi-directional

        self.nodes[from_node.label] = from_node
        self.nodes[to_node.label] = to_node
        self.edges[from_node.label].add(to_node.label)
        self.edges[to_node.label].add(from_node.label)
        self.weights[f"{from_node.label}-{to_node.label}"] = weight
        self.weights[f"{to_node.label}-{from_node.label}"] = weight

    def nodes_to_csv(self, file_name=None, path=None):
        all_nodes = [(self.nodes[node].x, self.nodes[node].y, self.nodes[node].label) for node in self.nodes]
        if path is not None:
            if file_name is None:
                file_name = "shortest_path.csv"
            all_nodes = [(self.nodes[node].x, self.nodes[node].y, self.nodes[node].label) for node in path]
        if file_name is None:
            file_name = "nodes.csv"

        headers = ['X', 'Y', 'L']
        try:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(all_nodes)
        except FileExistsError:
            print("Could not export")
        else:
            print("exported nodes successfully")

    @staticmethod
    def node_to_csv(node, file_name="closest_node.csv"):

        headers = ['X', 'Y', 'L']
        try:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows([[node.x, node.y, node.label]])
        except FileExistsError:
            print("Could not export")
        else:
            print("exported node successfully")

    def query_closest_location(self, x, y, label):
        other_node = Node(x=x, y=y, label=label)

        return min(
            [(self.get_weight(other_node, self.nodes[node]), self.nodes[node]) for node in self.nodes])

    @staticmethod
    def get_weight(from_node: Node, to_node: Node) -> float:
        # Euclidean distance
        delta_y = to_node.y - from_node.y
        delta_x = to_node.x - from_node.x
        return math.sqrt((delta_y ** 2 + delta_x ** 2))
