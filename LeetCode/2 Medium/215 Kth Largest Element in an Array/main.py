from typing import List


class MinHeap:
    def __init__(self, k: int):
        self.items = []
        self.size = 0

        self.k = k

    def percolate_up(self, i: int):
        parent = (i + 1) // 2 - 1

        if parent >= 0 and self.items[parent] > self.items[i]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]

            self.percolate_up(parent)

    def percolate_down(self, i: int):
        left = 2 * (i + 1) - 1
        right = 2 * (i + 1)

        smallest = i

        if left < self.size and self.items[left] < self.items[i]:
            smallest = left
        if right < self.size and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]

            self.percolate_down(smallest)

    def delete_min(self) -> int:
        minn = self.items[0]
        last = self.items.pop()
        self.items[0] = last
        self.size -= 1

        self.percolate_down(0)

        return minn

    def insert(self, val: int) -> int:
        self.items.append(val)
        self.size += 1

        self.percolate_up(self.size - 1)

        if self.size > self.k:
            self.delete_min()

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.items[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap(k)

        for num in nums:
            # print(heap.items)
            heap.insert(num)

        return heap.peek()


if __name__ == "__main__":
    sol = Solution()

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sol.findKthLargest(nums, k))

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(sol.findKthLargest(nums, k))
