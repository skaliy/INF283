#https://stackoverflow.com/questions/2482602/a-general-tree-implementation

class Node(object):
    
    def __init__(self):
        self.data = None
        self.children = {}
        self.isLeaf = False
        self.parent_node = None
        self.category = None

    def add_child(self, variable_name, node):
        self.children[variable_name] = node
