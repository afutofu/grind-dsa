# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p != None and q == None:
            return False
        if p == None and q != None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


if __name__ == "__main__":
    s = Solution()

    # Example 1
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert s.isSameTree(p, q) == True
    print(s.isSameTree(p, q))

    # Example 2
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert s.isSameTree(p, q) == False
    print(s.isSameTree(p, q))
