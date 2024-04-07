class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Populate hash table
        for i in range(n):
            numMap[nums[i]] = i  # Populate map with elements and their indices

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        # If not found, return empty list
        return []
