from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        num_counter = {}

        # Iterate through the nums to get a count for each count
        for num in nums:
            if num in num_counter:
                num_counter[num] += 1
            else:
                num_counter[num] = 1

        # Find the majority element and return it
        num_length = len(nums)
        for num in num_counter:
            if num_counter[num] / num_length >= 0.5:
                return num
