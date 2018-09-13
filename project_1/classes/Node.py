#https://stackoverflow.com/questions/2482602/a-general-tree-implementation

class Node(object):
    
    def __init__(self):
        self.data = None
        self.children = []
        self.isChild = False
        self.parent_node = None

    def add_child(self, obj):
        self.children.append(obj)

