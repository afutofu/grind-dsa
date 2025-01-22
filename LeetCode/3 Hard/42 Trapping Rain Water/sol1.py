from typing import List


class Solution:

    # Get the tallest right wall from a start wall position
    def tallestRightWallIndex(self, height: List[int], start) -> int:
        lenHeight = len(height)

        p1 = start
        p2 = p1 + 1

        # Default to -1 to denote that right wall doesnt exist
        tallestRightWallIndex = -1
        tallestRightWall = 0

        while p2 < lenHeight:
            p1h = height[p1]
            p2h = height[p2]

            # Hit a right wall that is taller than the start wall
            if p1h <= p2h:
                # print("wut")
                return p2
            elif p2h > 0:
                if p2h >= tallestRightWall:
                    tallestRightWall = p2h
                    tallestRightWallIndex = p2

            p2 += 1

        return tallestRightWallIndex

    def trap(self, height: List[int]) -> int:
        lenHeight = len(height)
        if lenHeight == 1:
            return 0

        mArea = 0
        cArea = 0

        p1 = 0
        p2 = 1

        while p2 < lenHeight:
            p1h = height[p1]
            p2h = height[p2]

            # print(p1, p2)

            # Edge case for starting with empty
            if p1 == 0 and p2h > p1h:
                p1 = p2
                p2 += 1
                continue
            elif p1 == 0 and p2h == 0:
                p2 += 1
                continue

            # If a wall is encountered
            if p1h > 0:

                # Find the right wall to trap water
                p2 = self.tallestRightWallIndex(height, p1)

                # print(p2)

                # If no next tallest wall,
                # Break out of loop
                if p2 == -1:
                    p2 = lenHeight
                    break

                # If next tallest wall is next,
                # incrememnt pointers and continue
                if p2 - p1 == 1:
                    p1 += 1
                    p2 += 1
                    continue

                rightWallHeight = height[p2]

                subContainerHeight = min(p1h, rightWallHeight)

                p1 += 1

                # Add the area
                while p1 < p2:
                    p1h = height[p1]
                    cArea += subContainerHeight - p1h
                    p1 += 1

                # Move pointers
                p1 = p2
                p2 = p1 + 1

                # Add to max area
                # print("cArea", cArea)
                mArea += cArea
                cArea = 0

        # print(mArea)

        return mArea


if __name__ == "__main__":
    s = Solution()

    # Example 1
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert s.trap(height) == 6

    # Example 2
    height = [4, 2, 0, 3, 2, 5]
    assert s.trap(height) == 9

    # Example 3
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert s.trap(height) == 6

    # Example 4
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert s.trap(height) == 6

    print("All passed")
