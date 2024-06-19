from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        # print(res)
        return res

    def dfs(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path)
            return

        for i in range(len(nums)):
            if nums[i] in path:
                continue
            else:
                self.dfs(nums, path + [nums[i]], res)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    # Input: nums = [1,2,3]
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(
        s.permute([1, 2, 3])
    )  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    # Example 2
    # Input: nums = [0,1]
    # Output: [[0,1],[1,0]]
    print(s.permute([0, 1]))  # [[0, 1], [1, 0]]

    # Example 3
    # Input: nums = [1]
    # Output: [[1]]
    print(s.permute([1]))  # [[1]]
