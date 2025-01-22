from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:
            print(s, token)
            if token != "+" and token != "-" and token != "*" and token != "/":
                s.append(int(token))
            else:
                operand2 = s.pop()
                operand1 = s.pop()

                if token == "+":
                    s.append(operand1 + operand2)
                elif token == "-":
                    s.append(operand1 - operand2)
                elif token == "*":
                    s.append(operand1 * operand2)
                elif token == "/":

                    if abs(operand1 / operand2) < 1:
                        s.append(0)
                    else:
                        # Integer division
                        if (
                            operand1 < 0
                            and operand2 >= 0
                            or operand1 >= 0
                            and operand2 < 0
                        ):
                            res = "-" + str((abs(operand1) // abs(operand2)))
                            print("weird division", res)
                            s.append(int(res))
                        else:
                            s.append(operand1 // operand2)

        # print(s)

        return s[0]


if __name__ == "__main__":
    s = Solution()

    # Example 1
    tokens = ["2", "1", "+", "3", "*"]
    assert s.evalRPN(tokens) == 9

    # Example 2
    tokens = ["4", "13", "5", "/", "+"]
    assert s.evalRPN(tokens) == 6

    # Example 5
    tokens = ["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert s.evalRPN(tokens) == 22

    print("All passed")
