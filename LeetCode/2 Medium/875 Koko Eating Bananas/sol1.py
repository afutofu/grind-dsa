import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highest = None
        for pile in piles:
            if highest == None or highest < pile:
                highest = pile

        l = 0
        r = highest

        best_k = highest
        best_hours = len(piles)

        while l <= r:
            k = (l + r) // 2
            # print(l, r, k, best_k)

            if k == 0:
                k = 1
                # break

            hours = 0
            for pile in piles:
                bananas = pile
                # print('compute', bananas, k, hours)

                if k == 1:
                    hours += bananas
                    continue

                hours += math.ceil(bananas / k)

                # while bananas > 0:
                #     bananas -= k
                #     hours += 1

            # print("hours", hours)

            if k < best_k and hours <= h:
                best_k = k
                r = k - 1
            else:
                l = k + 1

        print("best_k", best_k)

        return best_k


if __name__ == "__main__":
    s = Solution()

    # Example 1
    piles = [3, 6, 7, 11]
    h = 8
    assert s.minEatingSpeed(piles, h) == 4

    # Example 2
    piles = [30, 11, 23, 4, 20]
    h = 5
    assert s.minEatingSpeed(piles, h) == 30

    # Example 3
    piles = [30, 11, 23, 4, 20]
    h = 6
    assert s.minEatingSpeed(piles, h) == 23

    print("All passed")
