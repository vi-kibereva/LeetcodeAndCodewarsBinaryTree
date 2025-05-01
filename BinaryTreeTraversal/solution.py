class Node:
    def __init__(self, data, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
def pre_order(node):
    result = []
    def traverse(node):
        if node:
            result.append(node.data)
            traverse(node.left)
            traverse(node.right)
    traverse(node)
    return result


def in_order(node):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.data)
            traverse(node.right)
    traverse(node)
    return result

def post_order(node):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.data)
    traverse(node)
    return result

