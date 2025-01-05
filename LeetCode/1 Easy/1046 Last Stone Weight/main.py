from typing import List


class MaxHeap:
    def __init__(self, nums: List[int]) -> None:
        self.heap = nums
        self.size = len(nums)

        self.build_heap()

    def build_heap(self) -> None:
        for i in range(self.size // 2, -1, -1):
            self.percolate_down(i)

    def percolate_up(self, i: int) -> None:
        parent = (i + 1) // 2 - 1

        if parent >= 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

            self.percolate_up(parent)

    def percolate_down(self, i: int) -> None:
        left = 2 * (i + 1) - 1
        right = 2 * (i + 1)

        biggest = i

        if left < self.size and self.heap[left] > self.heap[i]:
            biggest = left
        if right < self.size and self.heap[right] > self.heap[biggest]:
            biggest = right

        if biggest != i:
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i]

            self.percolate_down(biggest)

    def insert(self, val: int) -> None:
        self.heap.append(val)
        self.size += 1

        self.percolate_up(self.size - 1)

    def delete_max(self) -> int:
        if self.size == 0:
            return -1
        elif self.size == 1:
            self.size -= 1
            return self.heap.pop()

        maxx = self.heap[0]
        last = self.heap.pop()
        self.heap[0] = last

        self.size -= 1

        self.percolate_down(0)

        return maxx


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap(stones)

        # print(heap.heap)

        while heap.size > 1:
            first = heap.delete_max()
            second = heap.delete_max()

            diff = abs(first - second)

            print(heap.heap, first, second, diff, heap.size)

            if diff > 0:
                heap.insert(diff)

        return heap.heap[0] if heap.size > 0 else 0


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]

    s = Solution()
    print(s.lastStoneWeight(stones))

    # More test cases
    stones = [2, 2]
    print(s.lastStoneWeight(stones))

    stones = [1, 3]
    print(s.lastStoneWeight(stones))

    stones = [1, 3, 3]
    print(s.lastStoneWeight(stones))

    stones = [1, 3, 3, 3]
    print(s.lastStoneWeight(stones))

    stones = [1, 3, 3, 3, 3]
    print(s.lastStoneWeight(stones))
