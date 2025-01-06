from typing import List


class MaxHeap:
    def __init__(self):
        self.items = []
        self.size = 0

    def percolate_down(self, i: int):
        left = 2 * (i + 1) - 1
        right = 2 * (i + 1)

        largest = i
        if left < self.size and self.items[left][0] > self.items[i][0]:
            largest = left
        if right < self.size and self.items[right][0] > self.items[largest][0]:
            largest = right

        if largest != i:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]

            self.percolate_down(largest)

    def percolate_up(self, i: int):
        parent = (i + 1) // 2 - 1

        if parent >= 0 and self.items[parent][0] < self.items[i][0]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]

            self.percolate_up(parent)

    def pop(self) -> list[int, str]:
        if self.size == 0:
            raise Exception("Cannot pop from an empty heap")
        elif self.size == 1:
            self.size -= 1
            return self.items.pop()

        maxx = self.items[0]
        last = self.items.pop()
        self.items[0] = last

        self.size -= 1

        self.percolate_down(0)

        return maxx

    def insert(self, val: list[int, str]) -> None:
        self.items.append(val)
        self.size += 1

        self.percolate_up(self.size - 1)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mapp = {}

        # Store values in hash map
        for task in tasks:
            if task not in mapp:
                mapp[task] = 1
            else:
                mapp[task] += 1

        print(mapp)

        heap = MaxHeap()

        for i, k in enumerate(mapp):
            heap.insert([mapp[k], k])

        print(heap.items)

        queue = []

        time = 1

        while len(queue) > 0 or len(heap.items) > 0:
            # print(time, heap.items, queue)
            # Decrement cycles in queue
            for cooldown_task in queue:
                cooldown_task[0] -= 1

            if heap.size > 0:
                process_task = heap.pop()

                if process_task[0] > 1:
                    queue.append([n, process_task])

            if len(queue) > 0 and queue[0][0] == 0:
                finish_process_task = queue.pop(0)[1]

                # Decrement frequency of task
                finish_process_task[0] -= 1

                # print('finish', finish_process_task)

                if finish_process_task[0] > 0:
                    heap.insert(finish_process_task)

            if len(queue) > 0 or len(heap.items) > 0:
                time += 1

        return time


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    sol = Solution()
    print(sol.leastInterval(tasks, n))

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    print(sol.leastInterval(tasks, n))

    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    print(sol.leastInterval(tasks, n))
