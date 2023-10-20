import unittest

from main import BinaryTree, binary_tree_diameter


class TestBinaryTreeDiameter(unittest.TestCase):
    def test_binary_tree_diameter(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)

        result = binary_tree_diameter(root)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()