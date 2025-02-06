from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(s):
            if s > target:
                return
            elif s == target:

                # Check if solution already exists
                sols = res.copy()
                newSol = subset.copy()

                # print(subset)

                # If no existing solution, put it in
                if len(sols) == 0:
                    res.append(subset.copy())
                    return

                # Else check for every other solution if it already exists
                for sol in sols:
                    sol = sol.copy()

                    for num in newSol:
                        if num in sol:
                            sol.remove(num)
                        else:
                            # If one solution doesnt match, check the others
                            break

                    # If the same solution already exists, return
                    if len(sol) == 0:
                        return

                # If no other solution exists, put it in
                res.append(subset.copy())

                return

            for num in nums:
                subset.append(num)
                dfs(s + num)
                subset.pop()

        dfs(0)

        # print(res)

        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1
    # Input: candidates = [2,3,6,7], target = 7
    # Output: [[2,2,3],[7]]
    print(s.combinationSum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]

    # Example 2
    # Input: candidates = [2,3,5], target = 8
    # Output: [[2,2,2,2],[2,3,3],[3,5]]
    print(s.combinationSum([2, 3, 5], 8))  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Example 3
    # Input: candidates = [2], target = 1
    # Output: []
    print(s.combinationSum([2], 1))  # []

    print("All passed")
