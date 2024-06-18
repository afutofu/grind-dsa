from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIdx = self.findMinIdx(nums)

        if target == nums[minIdx]:
            return minIdx

        n = len(nums)

        # Get left and right positions based on the value of the target
        left = minIdx if target <= nums[n - 1] else 0
        right = minIdx if target > nums[n - 1] else n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    # Binary search to find the smallest index in the array
    def findMinIdx(self, nums):
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(s.search(nums, target))  # 4

    # Example 2
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(s.search(nums, target))  # -1

    # Example 3
    nums = [1]
    target = 0
    print(s.search(nums, target))  # -1

    # Example 4
    nums = [1]
    target = 1
    print(s.search(nums, target))  # 0

    # Example 5
    nums = [3, 1]
    target = 1
    print(s.search(nums, target))  # 1
