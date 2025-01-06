# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if t1 == None and t2 == None:
            return True
        if t1 != None and t2 == None:
            return False
        if t1 == None and t2 != None:
            return False

        if t1.val == t2.val:
            return self.isSameTree(t1.left, t2.left) and self.isSameTree(
                t1.right, t2.right
            )
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        return (
            self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )


if __name__ == "__main__":
    s = Solution()

    # Example 1
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    assert s.isSubtree(root, subRoot) == True
    print(s.isSubtree(root, subRoot))

    # Example 2
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    assert s.isSubtree(root, subRoot) == False
    print(s.isSubtree(root, subRoot))

    # Example 3
    root = TreeNode(1, TreeNode(1))
    subRoot = TreeNode(1)
    assert s.isSubtree(root, subRoot) == True
    print(s.isSubtree(root, subRoot))

    # Example 4
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0)))
    assert s.isSubtree(root, subRoot) == True
    print(s.isSubtree(root, subRoot))

    # Example 5
    root = TreeNode(1, TreeNode(1))
    subRoot = TreeNode(1)
    assert s.isSubtree(root, subRoot) == True
    print(s.isSubtree(root, subRoot))
