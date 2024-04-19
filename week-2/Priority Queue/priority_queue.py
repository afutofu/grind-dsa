# Priority Queue implementation using a heap data structure
class PriorityQueue:
    # 0-indexed min heap
    heap: list = []
    size: int = 0

    def __init__(self, heap: list) -> None:
        self.heap = heap
        self.size = len(heap)

        # Build the heap
        self.build_heap()

    def build_heap(self) -> None:
        for i in range(len(self.heap) // 2, -1, -1):
            self.percolate_down(i)

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self.size += 1

        self.percolate_up(self.size - 1)

    def delete_min(self) -> int:
        min = self.heap[0]
        br = self.heap.pop()

        self.size -= 1

        self.heap[0] = br
        self.percolate_down(0)

        return min

    def percolate_up(self, index: int) -> None:
        parent = (index - 1) // 2 - 1

        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.percolate_up(parent)

    def percolate_down(self, index: int) -> None:
        left = 2 * (index + 1) - 1
        right = 2 * (index + 1)

        smallest = index

        if left < self.size and self.heap[left] < self.heap[index]:
            smallest = left

        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self.percolate_down(smallest)


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
