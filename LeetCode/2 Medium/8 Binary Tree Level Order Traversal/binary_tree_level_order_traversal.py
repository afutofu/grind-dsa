from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    result = []

    def traverse(self, root, level):
        if root == None:
            return None

        val = root.val

        if len(self.result) > level:
            self.result[level].append(val)
        else:
            self.result.append([val])

        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)

        return root

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        self.result = []
        self.traverse(root, 0)

        return self.result
