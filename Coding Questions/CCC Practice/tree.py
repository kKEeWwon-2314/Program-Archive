"""
A basic tree in Python 3.9


class Tree(object):
    def __init__(self):
        self.name = None
        self.children = []
        self.previous = None
        self.info = None

    def prev(self):
        return self.previous
    
    def next(self, child):
        return self.children[child]

    def add_node(self):
        node = Tree()
        self.children.append(node)
        node.prev = self
        return node

    def get_attributes(self, node_name):
        for child in range(len(self.children)):
            if (self.children[child].name == node_name):
                return self.children[child]
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def post_tree_inorder(node):
    if (node != None):
        return None
    else:
        post_tree_inorder(node.left)
        print(node.val)
        post_tree_inorder(node.right)

def post_tree_postorder(node):
    if (node != None):
        return None
    else:
        post_tree_inorder(node.left)
        post_tree_inorder(node.right)
        print(node.val)

def post_tree_postorder(node):
    if (node != None):
        return None
    else:
        print(node.val)
        post_tree_inorder(node.left)
        post_tree_inorder(node.right)
        