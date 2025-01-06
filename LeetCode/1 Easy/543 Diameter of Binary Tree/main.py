# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getMaxDepth(self, root: Optional[TreeNode], maxDepth) -> int:
        if root == None:
            return maxDepth

        l = 0
        r = 0

        # print(root.val, maxDepth)

        l = self.getMaxDepth(root.left, maxDepth + 1)
        r = self.getMaxDepth(root.right, maxDepth + 1)

        return max(l, r)

    def helper(self, root: Optional[TreeNode], maxDiameter) -> int:
        if root == None:
            return maxDiameter

        l = 0
        r = 0

        if root.left != None:
            l = self.getMaxDepth(root.left, 0)

        if root.right != None:
            r = self.getMaxDepth(root.right, 0)

        # print(l, r)

        maxDiameter = max(l + r, maxDiameter)

        if root.left != None:
            maxDiameter = max(maxDiameter, self.helper(root.left, maxDiameter))

        if root.right != None:
            maxDiameter = max(maxDiameter, self.helper(root.right, maxDiameter))

        return maxDiameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return 0

        return self.helper(root, 0)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert s.diameterOfBinaryTree(root) == 2
    print(s.diameterOfBinaryTree(root))

    # Example 2
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert s.diameterOfBinaryTree(root) == 3
    print(s.diameterOfBinaryTree(root))

    # Example 3
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7))))))
    assert s.diameterOfBinaryTree(root) == 5
    print(s.diameterOfBinaryTree(root))
