"""
Problem: Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

import unittest
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    """Build a binary tree from level-order list (None for missing nodes)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

class Solution:
    """
    Approach: Recursive inorder traversal.
    Time complexity: O(n)
    Space complexity: O(n) due to recursion stack
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorder(root, result)
        return result

    def _inorder(self, node: Optional[TreeNode], result: List[int]) -> None:
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)

class TestInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = build_tree([1, None, 2, 3])
        self.assertEqual(self.sol.inorderTraversal(root), [1,3,2])

    def test_example2(self):
        root = build_tree([])
        self.assertEqual(self.sol.inorderTraversal(root), [])

    def test_example3(self):
        root = build_tree([1])
        self.assertEqual(self.sol.inorderTraversal(root), [1])

    def test_balanced_tree(self):
       
        root = build_tree([1,2,3,4,5,None,6])
        self.assertEqual(self.sol.inorderTraversal(root), [4,2,5,1,3,6])

    def test_left_skewed(self):
        root = build_tree([1,2,None,3,None,4])
        self.assertEqual(self.sol.inorderTraversal(root), [4,3,2,1])

    def test_right_skewed(self):
        root = build_tree([1,None,2,None,3,None,4])
        self.assertEqual(self.sol.inorderTraversal(root), [1,2,3,4])

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
    # Manual demo
    sol = Solution()
    root = build_tree([1, None, 2, 3])
    print(sol.inorderTraversal(root))