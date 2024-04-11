class MyQueue:

    def __init__(self):
        # Use stack 1 to push elements and stack 2 to pop elements
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        # Reverse stack1 order by popping each value and appending it to stack2 (making it FIFO)
        stackLen = len(self.stack1)
        for i in range(stackLen):
            self.stack2.append(self.stack1.pop())

        # Save the popped item
        popped_item = self.stack2.pop()

        # Reverse the stack2 order by popping each value and appending it to stack1 (making it FILO)
        for i in range(stackLen - 1):
            self.stack1.append(self.stack2.pop())

        return popped_item

    # Return the first element in the stack1 as it is the first element next in the queue
    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
