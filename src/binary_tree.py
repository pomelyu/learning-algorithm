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
        root = self.get_root()
        stack = [root]
        output = []
        while len(stack) != 0:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return output

    
    def in_order_traverse(self):
        root = self.get_root()
        stack = []
        ptr = root
        output = []
        while len(stack) != 0 or ptr:
            while ptr:
                stack.append(ptr)
                ptr = ptr.left
            ptr = stack.pop()
            output.append(ptr.val)
            ptr = ptr.right

        return output

    def post_order_traverse(self):
        return self.post_order_traverse_recursive(self.get_root())
    
    def post_order_traverse_recursive(self, node):
        if not node:
            return []

        left_order = self.post_order_traverse_recursive(node.left)
        right_order = self.post_order_traverse_recursive(node.right)
        return left_order + right_order + [node.val]
        