class Node(object):

    def __init__(self, point_id=None, label=None, x=None, y=None):
        self.point_id = point_id
        self.label = label
        self.x = x
        self.y = y


class NodeContainer(object):

    def __init__(self):
        self.container = []

    def add_node(self, node: Node):
        self.container.append(node)
