# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case: If the current node does not exist
        if root == None:
            return root

        # Call the left substree
        self.invertTree(root.left)

        # Call the right substree
        self.invertTree(root.right)

        # Swap the nodes
        root.left, root.right = root.right, root.left

        # Return the root
        return root
