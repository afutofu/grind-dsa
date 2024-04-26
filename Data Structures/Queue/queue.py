class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.hd = None
        self.tl = None
        self.size = 0

    def enqueue(self, data) -> None:
        node = Node(data)

        if self.size > 0:
            self.tl.next = node
            self.tl = self.tl.next
        else:
            self.hd = node
            self.tl = node

        self.size += 1

    def dequeue(self) -> None:
        if self.size == 0:
            return None

        node = self.hd
        self.hd = self.hd.next
        self.size -= 1

        return node.data

    def __str__(self) -> str:
        if self.size == 0:
            return "Queue is empty"

        curr = self.hd
        res = ""

        while curr:
            res += str(curr.data) + " -> "
            curr = curr.next

        return res + "None"

    def is_empty(self) -> bool:
        return self.size == 0


if __name__ == "__main__":
    q = Queue()

    print("Enqueue 1")
    q.enqueue(1)
    print(q)

    print("Enqueue 2")
    q.enqueue(2)
    print(q)

    print("Dequeue")
    q.dequeue()
    print(q)

    print("Enqueue 3")
    q.enqueue(3)
    print(q)
