class BinaryTreeNode():
   def  __init__(self, val):
       self.val = val
       self.left = None
       self.right = None


class BinaryTree():
    def __init__(self, root_value):
        self.root = BinaryTreeNode(root_value)

    def get_root(self):
        return self.root

    def insert_left(self, node, val):
        tree_node = BinaryTreeNode(val)
        node.left = tree_node
        return tree_node

    def insert_right(self, node, val):
        tree_node = BinaryTreeNode(val)
        node.right = tree_node
        return tree_node

    def pre_order_traverse(self):
        # TODO:
        pass
    
    def in_order_traverse(self):
        # TODO:
        pass

    def post_order_traverse(self):
        # TODO:
        pass
