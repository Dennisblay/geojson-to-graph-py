from collections import defaultdict


class Graph(object):
    class Node(object):

        def __init__(self, point_id=None, name=None, x=None, y=None):
            self.point_id = point_id
            self.name = name
            self.x = x
            self.y = y

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

    def add_node(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
