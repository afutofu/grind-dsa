# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMaxHeight(self, root):
        if root == None:
            return 0

        leftHeight = self.getMaxHeight(root.left)
        rightHeight = self.getMaxHeight(root.right)

        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1

        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.getMaxHeight(root) != -1
