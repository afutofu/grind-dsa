from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten_list = []

        for sublist in matrix:
            for num in sublist:
                flatten_list.append(num)

        # print(flatten_list)

        if len(flatten_list) == 0:
            if flatten_list[0] == target:
                return True
            else:
                return False

        # Binary search on the flatten list
        l = 0
        r = len(flatten_list) - 1

        while l <= r:
            mid = (l + r) // 2

            if flatten_list[mid] < target:
                l = mid + 1
            elif flatten_list[mid] > target:
                r = mid - 1
            else:
                return True

        return False


if __name__ == "__main__":
    s = Solution()

    # Example 1
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert s.searchMatrix(matrix, target) == True

    # Example 2
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert s.searchMatrix(matrix, target) == False

    # Example 3
    matrix = [[1]]
    target = 1
    assert s.searchMatrix(matrix, target) == True

    print("All passed")
