#https://stackoverflow.com/questions/2482602/a-general-tree-implementation

class Node(object):
    
    def __init__(self):
        self.data = None
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

