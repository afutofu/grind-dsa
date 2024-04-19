from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        i = 0
        while len(tokens) > 1:
            if tokens[i] == "+":
                i -= 2
                num1 = float(tokens.pop(i))
                num2 = float(tokens.pop(i))

                tokens[i] = num1 + num2
            elif tokens[i] == "-":
                i -= 2
                num1 = float(tokens.pop(i))
                num2 = float(tokens.pop(i))

                tokens[i] = num1 - num2
            elif tokens[i] == "*":
                i -= 2
                num1 = float(tokens.pop(i))
                num2 = float(tokens.pop(i))

                tokens[i] = num1 * num2
            elif tokens[i] == "/":
                i -= 2
                num1 = float(tokens.pop(i))
                num2 = float(tokens.pop(i))

                tokens[i] = int(num1 / num2)

            i += 1

        print(tokens)
        return int(tokens[0])
