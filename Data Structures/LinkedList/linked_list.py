class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def update(self, data, value):
        current = self.head
        while current:
            if current.data == data:
                current.data = value
                return
            current = current.next

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.data) + " -> "
            current = current.next
        return result + "None"


# LinkedList using (key, value) as data
class KVLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def update(self, key, value):
        current = self.head
        while current:
            if current.data[0] == key:
                current.data[1] = value
                return
            current = current.next

    def delete(self, key):
        if self.head is None:
            return
        if self.head.data[0] == key:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data[0] == key:
                current.next = current.next.next
                return
            current = current.next

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.data) + " -> "
            current = current.next
        return result + "None"


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.prepend(0)
    ll.delete(3)
    print(ll)
