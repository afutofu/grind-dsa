from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        numsLen = len(nums)

        if numsLen == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if numsLen == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        l = 0
        r = numsLen - 1

        while l <= r:
            mid = (r + l) // 2

            el1 = nums[l]
            el2 = nums[r]
            elMid = nums[mid]

            if elMid == target:
                # Return index if found
                return mid

            if el1 < el2:
                # Sorted, do regular binary search
                if elMid < target:
                    l = mid + 1
                elif elMid > target:
                    r = mid - 1
            else:
                # Not sorted
                if mid > 0 and target == nums[mid - 1]:
                    return mid - 1
                elif mid < numsLen - 1 and target == nums[mid + 1]:
                    return mid + 1

                if target < elMid and nums[0] > elMid:
                    # Target is in left half
                    r = mid - 1
                else:
                    # target > elMid

                    l = mid + 1

        return -1


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert s.search(nums, target) == 4

    # Example 2
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    assert s.search(nums, target) == -1

    # Example 3
    nums = [1]
    target = 0
    assert s.search(nums, target) == -1

    # Example 4
    nums = [3, 1]
    target = 1
    assert s.search(nums, target) == 1

    # Example 5
    nums = [5, 1, 3]
    target = 5
    assert s.search(nums, target) == 0

    # Example 6
    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8
    assert s.search(nums, target) == 4

    # Example 7
    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 3
    assert s.search(nums, target) == 7

    # Example 8
    nums = [1, 3]
    target = 3
    assert s.search(nums, target) == 1

    # Example 9
    nums = [1, 3]
    target = 1
    assert s.search(nums, target) == 0

    # Example 10
    nums = [3, 1]
    target = 3
    assert s.search(nums, target) == 0

    # Example 11
    nums = [3, 1]
    target = 1
    assert s.search(nums, target) == 1

    # Example 12
    nums = [3, 1, 2]
    target = 1
    assert s.search(nums, target) == 1

    # Example 13
    nums = [3, 1, 2]
    target = 2
    assert s.search(nums, target) == 2

    print("All passed")
