# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDepth(self, root: Optional[TreeNode], d) -> int:
        if root == None:
            return d
        # print(root.val, d)

        left_depth = self.getDepth(root.left, d + 1)
        right_depth = self.getDepth(root.right, d + 1)

        return max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root, 0)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert s.maxDepth(root) == 3
    print(s.maxDepth(root))

    # Example 2
    root = TreeNode(1, None, TreeNode(2))
    assert s.maxDepth(root) == 2
    print(s.maxDepth(root))

    # Example 3
    root = None
    assert s.maxDepth(root) == 0
    print(s.maxDepth(root))

    # Example 4
    root = TreeNode(0)
    assert s.maxDepth(root) == 1
    print(s.maxDepth(root))
