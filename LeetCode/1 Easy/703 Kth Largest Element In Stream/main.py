from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.size = len(nums)
        self.k = k
        self.build_heap()

    def build_heap(self):
        # Percolate down ignoring leaf nodes
        for i in range(len(self.heap) // 2, -1, -1):
            self.percolate_down(i)

        while len(self.heap) > self.k:
            self.delete_min()

    def percolate_up(self, index: int):
        parent = (index + 1) // 2 - 1

        if parent >= 0 and self.heap[parent] > self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp

            self.percolate_up(parent)

    def percolate_down(self, index: int):
        left = 2 * (index + 1) - 1
        right = 2 * (index + 1)

        smallest = index

        if left < self.size and self.heap[left] < self.heap[index]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            temp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = temp

            self.percolate_down(smallest)

    def delete_min(self) -> int:
        if self.size == 0:
            return None
        elif self.size == 1:
            self.size -= 1
            return self.heap.pop

        # Pop last node, set it to new root, then percolate it down
        minn = self.heap[0]
        last_node = self.heap.pop()
        self.heap[0] = last_node

        self.size -= 1

        self.percolate_down(0)

        return minn

    def add(self, val: int) -> int:
        print("before delete", self.heap)

        self.heap.append(val)
        self.size += 1

        self.percolate_up(self.size - 1)

        if self.size > self.k:
            self.delete_min()

        print(self.heap)

        return self.heap[0]


if __name__ == "__main__":
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    print(kth_largest.add(3))
    print(kth_largest.add(5))
    print(kth_largest.add(10))
    print(kth_largest.add(9))
    print(kth_largest.add(4))
    print(kth_largest.add(1))
    print(kth_largest.add(7))
    print(kth_largest.add(6))
    print(kth_largest.add(2))
    print(kth_largest.add(8))
    print(kth_largest.add(10))
    print(kth_largest.add(1))
    print(kth_largest.add(3))
    print(kth_largest.add(2))
    print(kth_largest.add(4))
    print(kth_largest.add(5))
    print(kth_largest.add(9))
    print(kth_largest.add(7))
    print(kth_largest.add(6))
    print(kth_largest.add(8))
    print(kth_largest.add(10))
