# Stack implementation


class Stack:
    def __init__(self):
        self.max_size = 10
        self.size = 0
        self.stack = [None for _ in range(self.max_size)]

    def push(self, value):
        self.stack[self.size] = value

        self.size += 1

        if self.size >= self.max_size - 1:
            self.resize()

    def pop(self):
        if self.size == 0:
            return None

        self.size -= 1

        return self.stack[self.size]

    def resize(self):
        self.max_size *= 2
        new_stack = [None for _ in range(self.max_size)]
        for i in range(self.size):
            new_stack[i] = self.stack[i]


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
