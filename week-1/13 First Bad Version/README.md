# First Bad Version

DS: Sorted array
Use: Binary search - ish

- Since input is length of sorted array from 1 to n, we can use binary search to find the first bad version
- If the mid point is a bad version, then check whether the direct left of it is True (if so return mid - 1), else set the new high = mid - 1 (because we want to eliminate the right half)
- If the mid point is a good version, then check whether the direct right of it is False (if so return mid + 1), else se the new low = mid + 1 (to eliminate the lef thalf)
- The problem guarantees that there is always a bad version so we don't have an else case
