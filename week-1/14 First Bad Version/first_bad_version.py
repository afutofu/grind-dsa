# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def isBadVersion(version: int) -> bool:
    pass


class Solution:

    def firstBadVersion(self, n: int) -> int:

        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            isMidVersionBad = isBadVersion(mid)

            if isMidVersionBad:
                if isBadVersion(mid - 1) == False:
                    return mid
                high = mid - 1
            else:
                if isBadVersion(mid + 1) == True:
                    return mid + 1
                low = mid + 1
