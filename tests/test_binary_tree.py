from src.binary_tree import BinaryTree

def test_tree_init():
    root_val = 0
    tree = BinaryTree(root_val)
    tree_root = tree.get_root()

    assert tree_root.val == root_val
    assert tree_root.left == None
    assert tree_root.right == None

def test_tree_insert():
    root_val = 0
    tree = BinaryTree(root_val)
    tree_root = tree.get_root()

    node_1 = tree.insert_left(tree_root, 1)
    node_2 = tree.insert_right(tree_root, 2)

    assert node_1.val == 1
    assert node_2.val == 2
    assert tree_root.left == node_1
    assert tree_root.right == node_2

    assert tree_root.left.val == 1
    assert tree_root.right.val == 2
