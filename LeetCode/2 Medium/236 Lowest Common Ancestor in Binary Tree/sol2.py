# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(
        self, root: TreeNode, p: TreeNode, q: TreeNode, ancestor: TreeNode
    ) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return ancestor

        low = 0
        high = 0

        if p.val > q.val:
            low = q.val
            high = p.val
        else:
            low = p.val
            high = q.val

        if root.val < low:
            ancestor = self.helper(root.right, p, q, root.right)
        elif root.val > high:
            ancestor = self.helper(root.left, p, q, root.left)

        return ancestor

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        return self.helper(root, p, q, root)


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
