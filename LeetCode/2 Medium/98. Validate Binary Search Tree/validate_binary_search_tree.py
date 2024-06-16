# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        stack = []
        pre = None

        while root != None or len(stack) != 0:
            while root != None:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if pre != None and root.val <= pre.val:
                return False

            pre = root
            root = root.right

        return True


if __name__ == "__main__":
    # Example 1
    #     2
    #    / \
    #   1   3
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().isValidBST(root))  # True

    # Example 2
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(Solution().isValidBST(root))  # False

    # Example 3
    #     5
    #    / \
    #   4   6
    #      / \
    #     3   7
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    print(Solution().isValidBST(root))  # False

    # Example 4
    #     5
    #    / \
    #   1   7
    #      / \
    #     6   8
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    print(Solution().isValidBST(root))  # True

    # Example 5
    #     5
    #    / \
    #   1   7
    #      / \
    #     3   8
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(8)
    print(Solution().isValidBST(root))  # False
