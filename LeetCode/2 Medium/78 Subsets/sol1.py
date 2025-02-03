from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Decide to add nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Decide to NOT add nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)

        # print(res)

        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [1, 2, 3]
    assert len(s.subsets(nums)) == 8

    # Example 2
    nums = [0]
    assert len(s.subsets(nums)) == 2

    print("All passed")
