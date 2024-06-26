from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        oneDiffIntervals = []

        # Turn intervals into tuples of intervals that are each a difference of 1
        # Store unique values of the tuples in a list
        for interval in intervals:
            if interval[0] == interval[1] and interval not in oneDiffIntervals:
                oneDiffIntervals.append(interval)
                continue

            for point in range(interval[0], interval[1]):
                oneDiffInterval = [point, point + 1]

                if oneDiffInterval not in oneDiffIntervals:
                    oneDiffIntervals.append(oneDiffInterval)

        # print(oneDiffIntervals)
        # print(sorted(oneDiffIntervals))

        oneDiffIntervals = sorted(oneDiffIntervals)

        res = [oneDiffIntervals[0]]
        # Merge back the intervals
        for intervalIdx in range(1, len(oneDiffIntervals)):
            interval = oneDiffIntervals[intervalIdx]
            merged = False
            for existingIntervalIdx in range(len(res)):
                if interval[0] == res[existingIntervalIdx][1]:
                    res[existingIntervalIdx][1] = interval[1]
                    merged = True
                    break

            if not merged and interval not in res:
                res.append(interval)
            # print(res)

        return res


if __name__ == "__main__":
    print(
        Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    )  # [[1,6],[8,10],[15,18]]
    print(Solution().merge([[1, 4], [4, 5]]))  # [[1,5]]
    print(Solution().merge([[1, 4], [0, 4]]))  # [[0,4]]
    print(Solution().merge([[1, 4], [0, 0]]))  # [[0,0],[1,4]]
    print(Solution().merge([[1, 4], [0, 1]]))  # [[0,4]]
    print(Solution().merge([[1, 4], [0, 2]]))  # [[0,4]]
    print(Solution().merge([[1, 4], [0, 3]]))  # [[0,4]]
    print(Solution().merge([[1, 4], [2, 3]]))  # [[1,4]]
    print(Solution().merge([[1, 4], [3, 3]]))  # [[1,4]]
    print(Solution().merge([[1, 4], [4, 4]]))  # [[1,4]]
    print(Solution().merge([[1, 4], [5, 5]]))  # [[1,4],[5,5]]
    print(Solution().merge([[1, 4], [5, 6]]))  # [[1,4],[5,6]]
    print(Solution().merge([[1, 4], [6, 6]]))  # [[1,4],[6,6]]
    print(Solution().merge([[1, 4], [6, 7]]))  # [[1,4],[6,7]]
    print(Solution().merge([[1, 4], [7, 7]]))  # [[1,4],[7,7]]
    print(Solution().merge([[1, 4], [7, 8]]))  # [[1,4],[7,8]]
    print(Solution().merge([[1, 4], [8, 8]]))  # [[1,4],[8,8
