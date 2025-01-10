# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        stack = []
        temp = []
        res = 1

        stack.append((root, root.val))
        temp.append((root.val, root.val))

        while len(stack) > 0:
            curr = stack.pop()
            currTree = curr[0]
            currMax = curr[1]
            # print(currTree.val, currMax)

            if currTree.left != None:
                if currTree.left.val >= currMax:
                    res += 1

                newMax = max(currTree.left.val, currMax)
                stack.append((currTree.left, newMax))
                temp.append((currTree.left.val, newMax))

            if currTree.right != None:
                if currTree.right.val >= currMax:
                    res += 1

                newMax = max(currTree.right.val, currMax)
                stack.append((currTree.right, newMax))
                temp.append((currTree.right.val, newMax))

        # print(temp)

        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1
    root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    assert s.goodNodes(root) == 4
    print(s.goodNodes(root))

    # Example 2
    root = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
    assert s.goodNodes(root) == 3
    print(s.goodNodes(root))

    # Example 3
    root = TreeNode(1)
    assert s.goodNodes(root) == 1
    print(s.goodNodes(root))

    # Example 4
    root = TreeNode(2, TreeNode(4), TreeNode(3))
    assert s.goodNodes(root) == 3
    print(s.goodNodes(root))

    # Example 5
    root = TreeNode(2, TreeNode(1))
    assert s.goodNodes(root) == 1
    print(s.goodNodes(root))
