# Separate Chaining Hash Table implementation

import sys

sys.path.insert(1, "../LinkedList")


from linked_list import KVLinkedList


class HashTable:
    def __init__(self) -> None:
        self.max_size = 10
        self.size: float = 0
        self.table = [KVLinkedList() for _ in range(self.max_size)]
        self.load_factor = 0
        self.resize_count = 0
        self.prime_numbers = [7, 19, 37, 79, 157]

    def hash(self, key) -> int:
        return key % self.prime_numbers[self.resize_count]

    def resize(self, new_size) -> None:
        self.resize_count += 1
        self.size = 0
        old_table = self.table
        self.max_size = new_size
        self.table = [KVLinkedList() for _ in range(self.max_size)]
        for i in range(len(old_table)):
            current = old_table[i].head
            while current:
                self.insert(current.data[0], current.data[1])
                current = current.next

    def insert(self, key, value) -> None:
        index = self.hash(key)
        self.table[index].append((key, value))

        self.size += 1
        self.load_factor = self.size / self.max_size

        if self.load_factor >= 2:
            self.resize(self.max_size * 2)

    def update(self, key, value) -> None:
        index = self.hash(key)
        self.table[index].update(key, value)

    def delete(self, key) -> None:
        if self.size == 0:
            return

        index = self.hash(key)
        self.table[index].delete(key)

        self.size -= 1
        self.load_factor = self.size / self.max_size

    def search(self, key) -> int:
        index = self.hash(key)
        return self.table[index].search(key)

    def __str__(self) -> str:
        result = ""
        for i in range(self.max_size):
            result += f"{i}: {self.table[i]}\n"
        return result


# Test the HashTable implementation
if __name__ == "__main__":
    ht = HashTable()
    ht.insert(10, "A")
    ht.insert(20, "B")
    ht.insert(30, "C")
    ht.insert(40, "D")
    ht.insert(50, "E")
    ht.insert(60, "F")
    ht.insert(70, "G")
    ht.insert(80, "H")
    ht.insert(90, "I")
    ht.insert(100, "J")
    ht.insert(110, "K")
    ht.insert(120, "L")
    ht.insert(130, "M")
    ht.insert(140, "N")
    ht.insert(150, "O")
    ht.insert(160, "P")
    ht.insert(170, "Q")
    ht.insert(180, "R")
    ht.insert(190, "S")
    ht.insert(200, "T")
    print(ht)
    ht.delete(10)
    ht.delete(20)
    ht.delete(30)
    ht.delete(40)
    ht.delete(50)
    ht.delete(60)
    ht.delete(70)
    ht.delete(80)
    ht.delete(90)
    ht.delete(100)
    ht.delete(110)
    ht.delete(120)
    ht.delete(130)
    ht.delete(140)
    ht.delete(150)
    ht.delete(160)
    ht.delete(170)
    ht.delete(180)
    ht.delete(190)
    ht.delete(200)
    print(ht)
    ht.insert(10, "A")
    ht.insert(20, "B")
    ht.insert(30, "C")
    ht.insert(40, "D")
    ht.insert(50, "E")
    ht.insert(60, "F")
    ht.insert(70, "G")
    ht.insert(80, "H")
    ht.insert(90, "I")
    ht.insert(100, "J")
    ht.insert(110, "K")
    ht.insert(120, "L")
    ht.insert(130, "M")
    ht.insert(140, "N")
    ht.insert(150, "O")
    ht.insert(160, "P")
    ht.insert(170, "Q")
    ht.insert(180, "R")
    ht.insert(190, "S")
    ht.insert(200, "T")
    print(ht)
