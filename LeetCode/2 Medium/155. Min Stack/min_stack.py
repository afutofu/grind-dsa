class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []

    def push(self, val: int) -> None:
        if self.min == None or val < self.min:
            self.min = val

        self.stack.append((val, self.min))

    def pop(self) -> None:
        last = self.stack.pop()
        if len(self.stack) > 0:
            self.min = self.stack[len(self.stack) - 1][1]
        else:
            self.min = None

        return last[0]

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        return self.min


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # -3
    print(minStack.pop())  # -3
    print(minStack.top())  # 0
    print(minStack.getMin())  # -2
