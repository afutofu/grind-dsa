class Solution:
    def combinationSum(self, candidates, target):
        memo = []
        self.dfs(candidates, target, [], memo)
        return memo

    def dfs(self, nums, target, path, memo):
        if target < 0:
            return
        if target == 0:
            memo.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], memo)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    # Input: candidates = [2,3,6,7], target = 7
    # Output: [[2,2,3],[7]]
    # Explanation:
    # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    # 7 is a candidate, and 7 = 7.
    print(s.combinationSum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]

    # Example 2
    # Input: candidates = [2,3,5], target = 8
    # Output: [[2,2,2,2],[2,3,3],[3,5]]
    # Explanation:
    # 2, 3, and 5 are candidates, and 2 + 2 + 2 + 2 = 8.
    # 2 + 3 + 3 = 8.
    # 3 + 5 = 8.
    print(s.combinationSum([2, 3, 5], 8))  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
