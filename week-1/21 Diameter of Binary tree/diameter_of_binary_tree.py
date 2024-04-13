# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def get_depth(self, root) -> int:
        if root == None:
            return 0

        left = self.get_depth(root.left) if root.left else 0
        right = self.get_depth(root.right) if root.right else 0

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_depth(root)
        return self.diameter
