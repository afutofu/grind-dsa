# Definition for a binary tree node.
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        temp = []
        queue = []
        found = set()

        queue.append((root, 0))
        temp.append((root.val, 0))

        while len(queue) > 0:
            curr = queue.pop(0)

            # print(curr)

            if curr != None:
                if curr[0].left != None:
                    queue.append((curr[0].left, curr[1] + 1))
                    temp.append((curr[0].left.val, curr[1] + 1))

                if curr[0].right != None:
                    queue.append((curr[0].right, curr[1] + 1))
                    temp.append((curr[0].right.val, curr[1] + 1))

        # print(temp)

        res = []
        for t in temp:
            # print(res)
            if len(res) <= t[1]:
                res.append([t[0]])
            else:
                res[t[1]].append(t[0])

        # print(res)

        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]
    print(s.levelOrder(root))

    # Example 2
    root = TreeNode(1, None, TreeNode(2))
    assert s.levelOrder(root) == [[1], [2]]
    print(s.levelOrder(root))

    # Example 3
    root = None
    assert s.levelOrder(root) == []
    print(s.levelOrder(root))

    # Example 4
    root = TreeNode(0)
    assert s.levelOrder(root) == [[0]]
    print(s.levelOrder(root))
