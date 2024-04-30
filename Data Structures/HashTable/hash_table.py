# Separate Chaining Hash Table implementation

from LinkedList.linked_list import LinkedList


class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.table = [LinkedList() for _ in range(self.size)]

    def hash(self, key) -> int:
        return key % self.size

    def insert(self, key, value) -> None:
        index = self.hash(key)
        self.table[index].append((key, value))

    def delete(self, key) -> None:
        index = self.hash(key)
        self.table[index].delete(key)

    def search(self, key) -> int:
        index = self.hash(key)
        return self.table[index].search(key)

    def __str__(self) -> str:
        result = ""
        for i in range(self.size):
            result += f"{i}: {self.table[i]}\n"
        return result
