class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None:
            return False
        if node.val == key:
            return True
        if key < node.val:
            return self._find(node.left, key)
        return self._find(node.right, key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def __str__(self) -> str:
        return self._to_string(self.root)

    def _to_string(self, node):
        if node is None:
            return ""
        return f"{self._to_string(node.left)} {node.val} {self._to_string(node.right)}"


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print(bst.find(40))
    print(bst.find(90))

    print(bst)
