# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        queue = []
        temp = []

        queue.append((root, 0))
        temp.append((root.val, 0))

        while len(queue) > 0:
            curr = queue.pop(0)
            currTree = curr[0]
            currLevel = curr[1]

            if currTree.left != None:
                queue.append((currTree.left, currLevel + 1))
                temp.append((currTree.left.val, currLevel + 1))

            if currTree.right != None:
                queue.append((currTree.right, currLevel + 1))
                temp.append((currTree.right.val, currLevel + 1))

        # Filter to get the last element from each level
        res = []
        cLvl = None
        for i in range(len(temp) - 1, -1, -1):

            lvl = temp[i][1]
            val = temp[i][0]

            if i == 0:
                res.insert(0, val)
                continue

            if cLvl != lvl:
                res.insert(0, val)
                cLvl = lvl

        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert s.rightSideView(root) == [1, 3, 4]
    print(s.rightSideView(root))

    # Example 2
    root = TreeNode(1, None, TreeNode(3))
    assert s.rightSideView(root) == [1, 3]
    print(s.rightSideView(root))

    # Example 3
    root = None
    assert s.rightSideView(root) == []
    print(s.rightSideView(root))

    # Example 4
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert s.rightSideView(root) == [1, 3]
    print(s.rightSideView(root))

    # Example 5
    root = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4)))
    assert s.rightSideView(root) == [1, 3, 4]
    print(s.rightSideView(root))
