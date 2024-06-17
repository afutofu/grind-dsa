from typing import List


class Solution:
    visited = set()

    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        m = len(grid)  # no. of rows
        n = len(grid[0])  # no. of cols

        islandCount = 0

        for i in range(0, m):
            for j in range(0, n):
                xy = (j, i)

                # If coordinate is already visited, skip to the next
                if xy in self.visited:
                    continue

                curr = grid[i][j]
                print(xy, curr)

                if curr == "1":
                    # If a "1" is found, mark it as an island and explore adjacent "1"s
                    islandCount += 1
                    self.explore(j, i, grid, m, n)

        # print(self.visited)

        return islandCount

    def explore(self, x, y, grid, gridRows, gridCols):
        # BFS to check adjacent nodes till end of '1's

        xy = (x, y)

        if xy in self.visited:
            # Do nothing
            pass
        else:
            if grid[y][x] == "1":
                self.visited.add(xy)
                # Explore further if adjacent tiles arent edges
                # Explore left
                if x > 0:
                    self.explore(x - 1, y, grid, gridRows, gridCols)
                # Explore right
                if x < gridCols - 1:
                    self.explore(x + 1, y, grid, gridRows, gridCols)
                # Explore up
                if y > 0:
                    self.explore(x, y - 1, grid, gridRows, gridCols)
                # Explore down
                if y < gridRows - 1:
                    self.explore(x, y + 1, grid, gridRows, gridCols)


if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(s.numIslands(grid))  # 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(s.numIslands(grid))  # 3

    grid = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"],
    ]
    print(s.numIslands(grid))  # 1
