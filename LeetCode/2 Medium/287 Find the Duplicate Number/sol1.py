from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = len(nums)

        if l == 1:
            return -1
        if l == 2:
            if nums[0] == nums[1]:
                return nums[0]
            else:
                -1

        for i in range(l):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])

            nums[abs(nums[i]) - 1] *= -1


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [1, 3, 4, 2, 2]
    assert s.findDuplicate(nums) == 2

    # Example 2
    nums = [3, 1, 3, 4, 2]
    assert s.findDuplicate(nums) == 3

    # Example 3
    nums = [1, 1]
    assert s.findDuplicate(nums) == 1

    # Example 4
    nums = [1, 1, 2]
    assert s.findDuplicate(nums) == 1

    # Example 5
    nums = [2, 2, 2, 2, 2]
    assert s.findDuplicate(nums) == 2

    print("All passed")
