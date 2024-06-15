from typing import List


class Solution:
    memo = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        return self.helper(coins, amount)

    def helper(self, coins: List[int], amount: int) -> int:
        if amount in self.memo:
            return self.memo[amount]

        if amount == 0:
            answer = 0
        else:
            answer = -1
            for coin in coins:
                subproblem = amount - coin
                if subproblem < 0:
                    continue

                a = self.helper(coins, subproblem)

                if a == -1:
                    continue

                # If answer is -1 (initial value), set it to a (not -1) + 1
                if answer == -1:
                    answer = a + 1
                else:
                    # If answer is a value that isnt -1
                    answer = min(answer, a + 1)

        self.memo[amount] = answer
        return answer


if __name__ == "__main__":
    s = Solution()

    coins = [1, 2, 5]
    amount = 11

    print(s.coinChange(coins, amount))  # 3
