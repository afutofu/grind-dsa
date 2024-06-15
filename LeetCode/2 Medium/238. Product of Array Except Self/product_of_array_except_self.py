from typing import List


class Solution:
    # ex1 - [1,2,3,4]
    # ex1 - [-1,1,0,-3,3]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        output = []
        prefix = {0: 1, 1: nums[0]}
        suffix = {numLen - 1: 1, numLen - 2: nums[numLen - 1]}

        # prefix1 - 0: 1,   1: 1,    2: 2,   3: 6
        # suffix1 - 3: 1,   2: 4,    1: 12,  0: 24,
        # prefix2 - 0: 1    1: -1,   2: -1,  3: 0,  4: 0
        # suffix2 - 0: 0,   1: 0,    2: -9,  3: 3,  4: 1

        # Compute prefix
        for i in range(2, numLen):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        # Compute suffix
        for i in range(numLen - 3, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        # print(prefix)
        # print(suffix)

        for i in range(0, numLen):
            output.append(prefix[i] * suffix[i])

        return output


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [1, 2, 3, 4]
    print(s.productExceptSelf(nums))  # [24,12,8,6]

    # Example 2
    nums = [-1, 1, 0, -3, 3]
    print(s.productExceptSelf(nums))  # [0,0,9,0,0]
