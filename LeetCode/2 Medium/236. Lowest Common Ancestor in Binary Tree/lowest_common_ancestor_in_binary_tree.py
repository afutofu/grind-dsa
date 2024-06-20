# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    paths = {}

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        paths = {}
        self.findValPath(root, p.val, [])
        self.findValPath(root, q.val, [])

        lca = None
        for i in range(len(self.paths[p.val]) - 1, -1, -1):
            if self.paths[p.val][i] in self.paths[q.val]:
                lca = self.paths[p.val][i]
                break

        return lca

    def findValPath(self, root, val, path):
        if root == None:
            return
        if root.val == val:
            self.paths[val] = path + [root]
            return
        else:
            self.findValPath(root.left, val, path + [root])
            self.findValPath(root.right, val, path + [root])


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    p = root.left
    q = root.right
    print(Solution().lowestCommonAncestor(root, p, q).val)  # 3
