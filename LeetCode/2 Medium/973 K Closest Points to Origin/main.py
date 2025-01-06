import math
from typing import List


class MaxHeap:
    def __init__(self, k: int):
        self.items = []  # Tuple of ([int, int], int)
        self.size = 0
        self.k = k

    def percolate_up(self, i: int):
        parent = (i + 1) // 2 - 1

        if parent >= 0 and self.items[parent][1] < self.items[i][1]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]

            self.percolate_up(parent)

    def percolate_down(self, i: int):
        left = 2 * (i + 1) - 1
        right = 2 * (i + 1)

        largest = i

        if left < self.size and self.items[left][1] > self.items[i][1]:
            largest = left
        if right < self.size and self.items[right][1] > self.items[largest][1]:
            largest = right

        if largest != i:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]

            self.percolate_down(largest)

    def delete_max(self) -> int:
        maxx = self.items[0][0]
        last_item = self.items.pop()
        self.items[0] = last_item

        self.size -= 1

        self.percolate_down(0)

        return maxx

    def insert(self, val: List[int]):
        dist = math.sqrt(val[0] * val[0] + val[1] * val[1])

        self.items.append((val, dist))

        self.size += 1

        self.percolate_up(self.size - 1)

        if self.size > self.k:
            self.delete_max()

    def get_points(self) -> List[List[int]]:
        return list(map(lambda item: item[0], self.items))


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = MaxHeap(k)

        for point in points:
            # print(heap.items)
            heap.insert(point)

        return heap.get_points()


if __name__ == "__main__":
    sol = Solution()

    points = [[1, 3], [-2, 2]]
    k = 1
    print(sol.kClosest(points, k))

    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(sol.kClosest(points, k))

    points = [[1, 3], [-2, 2], [2, -2]]
    k = 2
    print(sol.kClosest(points, k))
