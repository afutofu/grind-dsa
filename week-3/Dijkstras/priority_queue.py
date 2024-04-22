# Priority Queue implementation using a heap data structure
# value = { priority: int, value: int }


from typing import Optional


class Item:
    def __init__(self, priority: int, value: int) -> None:
        self.priority = priority
        self.value = value

    def __lt__(self, other) -> bool:
        return self.priority < other.priority

    def __eq__(self, other) -> bool:
        return self.priority == other.priority

    def __repr__(self) -> str:
        return f"({self.priority}, {self.value})"


class PriorityQueue:
    # 0-indexed min heap
    heap: list[Item] = []
    size: int = 0

    def __init__(self, heap: list = None) -> None:
        if heap is None:
            self.heap = []
            self.size = 0
            return

        self.heap = heap
        self.size = len(heap)

        # Build the heap
        self.build_heap()

    def build_heap(self) -> None:
        # Build starting first ignoring the leaf nodes
        for i in range(len(self.heap) // 2, -1, -1):
            self.percolate_down(i)

    def insert(self, priority, value) -> None:
        # Insert the element at the end of the heap
        self.heap.append(Item(priority, value))
        self.size += 1

        # Percolate up the element to its correct position
        self.percolate_up(self.size - 1)
        print(self.heap)

    def delete_min(self) -> Item:
        if self.size == 0:
            return None
        elif self.size == 1:
            self.size -= 1
            return self.heap.pop()

        # Pop last node and set it as the new root
        min = self.heap[0]
        last_node = self.heap.pop()
        self.heap[0] = last_node

        self.size -= 1

        # Percolate down the new root to its correct position
        self.percolate_down(0)

        return min

    def percolate_up(self, index: int) -> None:
        parent = (index - 1) // 2 - 1

        # Swap the parent and the child if the parent is greater than the child
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.percolate_up(parent)

    def percolate_down(self, index: int) -> None:
        left = 2 * (index + 1) - 1
        right = 2 * (index + 1)

        smallest = index

        # Find the smallest element among the parent and its children
        if left < self.size and self.heap[left] < self.heap[index]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        # Swap the parent with the smallest child if either child is smaller than the parent
        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self.percolate_down(smallest)

    def decrease_key(self, new_priority: int, value: int) -> None:
        # Find the index of the element
        index = -1
        for i in range(self.size):
            if self.heap[i].value == value:
                index = i
                break

        # Update the priority of the element
        self.heap[index].priority = new_priority

        # Percolate up the element to its correct position
        self.percolate_up(index)

    def is_empty(self) -> bool:
        return self.size == 0


if "__main__" == __name__:
    print("This is a priority queue implementation")

    # Test the priority queue implementation
    pq = PriorityQueue([9, 5, 6, 2, 3])
    print(pq.heap)

    # Delete the minimum element
    pq.delete_min()
    print(pq.heap)

    # Insert a new element
    pq.insert(1)
    print(pq.heap)
