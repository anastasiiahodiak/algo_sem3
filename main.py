class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_diameter(tree: BinaryTree) -> int:
    def helper(node):
        if not node:
            return 0

        left_height = helper(node.left)
        right_height = helper(node.right)

        nonlocal max_diameter
        max_diameter = max(max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    max_diameter = 0
    helper(tree)
    return max_diameter