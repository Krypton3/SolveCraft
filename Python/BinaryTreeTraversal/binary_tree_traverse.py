# designing a class to make binary tree
class Tree():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# binary tree
def binary_tree():
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.right = Tree(6)
    return root


# pre order traversal
def pre_order_traverse(root):
    if root is None:
        return []
    return [root.val] + pre_order_traverse(root=root.left) + \
        pre_order_traverse(root=root.right)


# in order traversal
def in_order_traverse(root):
    if root is None:
        return []
    return in_order_traverse(root=root.left) + [root.val] + \
        in_order_traverse(root=root.right)


# post order traversal
def post_order_traverse(root):
    if root is None:
        return []
    return post_order_traverse(root=root.left) + \
        post_order_traverse(root=root.right) + [root.val]


root = binary_tree()
print("Pre-order Traversal:", post_order_traverse(root))
