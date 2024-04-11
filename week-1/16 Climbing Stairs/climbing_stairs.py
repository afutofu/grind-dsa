class Solution:
    def fastFib(self, n: int):
        if n == 0:
            return {"curr": 1, "prev": 0}

        fib: int = self.fastFib(n - 1)
        return {"curr": fib["curr"] + fib["prev"], "prev": fib["curr"]}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        return self.fastFib(n)["curr"]
