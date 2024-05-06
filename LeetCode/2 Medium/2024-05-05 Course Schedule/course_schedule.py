from typing import List


class Solution:
    def has_cycle(self, graph, curr, seen, done) -> bool:
        seen.add(curr)
        cycle_found = False
        for neighbor in graph[curr]:
            if neighbor in seen and neighbor not in done:
                cycle_found = True
            if neighbor not in seen and not cycle_found:
                cycle_found = self.has_cycle(graph, neighbor, seen, done)
        done.add(curr)
        return cycle_found

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 and numCourses > 0:
            return True

        # Turn prerequisities into an adjacency list
        adj_list = {}

        for i in range(numCourses):
            adj_list[i] = []

        for [a, b] in prerequisites:
            if a == b:
                return False
            if [b, a] in prerequisites:
                return False
            adj_list[b].append(a)

        seen = set()
        done = set()

        # For disconnected graphs, loop through each possible node
        for i in adj_list:
            if i not in done:
                cycle_found = self.has_cycle(adj_list, i, seen, done)

            if cycle_found:
                return False

        return not cycle_found


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))  # True
    print(s.canFinish(2, [[1, 0], [0, 1]]))  # False
    print(s.canFinish(3, [[1, 0], [2, 1]]))  # True
    print(s.canFinish(3, [[1, 0], [2, 1], [0, 2]]))  # False
    print(s.canFinish(3, [[1, 0], [2, 1], [0, 2], [2, 0]]))  # False
    print(s.canFinish(3, [[1, 0], [2, 1], [0, 2], [2, 0], [1, 2]]))  # False
    print(s.canFinish(3, [[1, 0], [2, 1], [0, 2], [2, 0], [1, 2], [0, 1]]))  # False
    print(
        s.canFinish(3, [[1, 0], [2, 1], [0, 2], [2, 0], [1, 2], [0, 1], [0, 2]])
    )  # False
    print(
        s.canFinish(3, [[1, 0], [2, 1], [0, 2], [2, 0], [1, 2], [0, 1], [0, 2], [1, 2]])
    )  # False
    print(
        s.canFinish(
            3, [[1, 0], [2, 1], [0, 2], [2, 0], [1, 2], [0, 1], [0, 2], [1, 2], [2, 1]]
        )
    )  # False
    print(
        s.canFinish(
            3,
            [
                [1, 0],
                [2, 1],
                [0, 2],
                [2, 0],
                [1, 2],
                [0, 1],
                [0, 2],
                [1, 2],
                [2, 1],
                [2, 0],
            ],
        )
    )  # False
