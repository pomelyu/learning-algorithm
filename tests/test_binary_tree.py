import pytest

from src.binary_tree import BinaryTree
from .reasons import REASON_TODO

@pytest.fixture
def demo_tree():
    tree = BinaryTree(0)
    tree_root = tree.get_root()

    node_1 = tree.insert_left(tree_root, 1)
    node_2 = tree.insert_right(tree_root, 2)
    node_3 = tree.insert_left(node_1, 3)
    tree.insert_right(node_3, 4)
    tree.insert_left(node_2, 5)
    tree.insert_right(node_2, 6)

    return tree


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

@pytest.mark.skip(reason=REASON_TODO)
def test_pre_order_traverse(demo_tree):
    output = demo_tree.pre_order_traverse()

    assert output == [0, 1, 3, 4, 2, 5, 6]

@pytest.mark.skip(reason=REASON_TODO)
def test_in_order_traverse(demo_tree):
    output = demo_tree.in_order_traverse()

    assert output == [3, 4, 1, 0, 5, 2, 6]

@pytest.mark.skip(reason=REASON_TODO)
def test_post_order_traverse(demo_tree):
    output = demo_tree.post_order_traverse()

    assert output == [6, 2, 5, 0, 1, 4, 3]
