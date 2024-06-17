from typing import List


class Solution:
    rottenXYs = set()

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # self.minutes = 0
        self.rottenXYs = set()
        m = len(grid)  # no of rows
        n = len(grid[0])  # no of cols

        # Get the coordinates for all the rotten oranges
        for y in range(0, m):
            for x in range(0, n):
                if grid[y][x] == 2:
                    self.rottenXYs.add((x, y))

        print(self.rottenXYs)

        minutes = 0

        # Start rotting adjacent oranges
        while True:
            oldLen = len(self.rottenXYs)

            # Create initial rotten XYs because the original may change during the loop
            initialRottenXYs = set(self.rottenXYs)

            for xy in initialRottenXYs:
                self.rot(xy[0], xy[1], grid, m, n)

            # Stop rotting if old length of rotten oranges is the same as after rotting
            if oldLen == len(self.rottenXYs):
                break

            minutes += 1

        # Return -1 if there are any fresh oranges left
        for y in range(0, m):
            for x in range(0, n):
                if grid[y][x] == 1:
                    return -1

        return minutes

    # Rot 4 directionally adjacent node from initial x y node
    def rot(self, x, y, grid, gridRows, gridCols):
        # Only rot if adjacent node is a fresh orange
        # Rot left
        if x > 0 and grid[y][x - 1] == 1:
            grid[y][x - 1] = 2
            self.rottenXYs.add((x - 1, y))
        # Rot right
        if x < gridCols - 1 and grid[y][x + 1] == 1:
            grid[y][x + 1] = 2
            self.rottenXYs.add((x + 1, y))
        # Rot up
        if y > 0 and grid[y - 1][x] == 1:
            grid[y - 1][x] = 2
            self.rottenXYs.add((x, y - 1))
        # Rot down
        if y < gridRows - 1 and grid[y + 1][x] == 1:
            grid[y + 1][x] = 2
            self.rottenXYs.add((x, y + 1))


if __name__ == "__main__":
    s = Solution()
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    print(s.orangesRotting(grid))  # 4

    grid = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1],
    ]
    print(s.orangesRotting(grid))  # -1

    grid = [
        [0, 2],
    ]
    print(s.orangesRotting(grid))  # 0

    grid = [
        [1, 2],
    ]
    print(s.orangesRotting(grid))  # 1

    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 2]]
    print(s.orangesRotting(grid))  # 2
