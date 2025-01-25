from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lenHeights = len(heights)

        if lenHeights == 2:
            return min(heights[0], heights[1])

        mArea = 0
        cArea = 0

        p1 = 0
        p2 = 1

        while p2 < lenHeights:
            cArea = (p2 - p1) * min(heights[p1], heights[p2])

            mArea = max(cArea, mArea)

            p2 += 1

            if p2 == lenHeights:
                p1 += 1
                p2 = p1 + 1

        return mArea


if __name__ == "__main__":
    s = Solution()

    # Example 1
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert s.maxArea(heights) == 49

    # Example 2
    heights = [1, 1]
    assert s.maxArea(heights) == 1

    # Example 3
    heights = [4, 3, 2, 1, 4]
    assert s.maxArea(heights) == 16

    # Example 4
    heights = [1, 2, 1]
    assert s.maxArea(heights) == 2

    # Example 5
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert s.maxArea(heights) == 49

    print("All passed")
