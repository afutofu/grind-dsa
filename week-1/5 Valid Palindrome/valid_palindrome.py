import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = re.sub("[\W_]+", "", s).lower()

        # Use a stack to compare the values of the latter half of the string
        stack = []
        length = len(cleanStr)
        isOdd = False
        if length % 2 == 1:
            isOdd = True

        for i in range(length):
            if isOdd and i == length // 2:
                continue

            if i >= length / 2:

                if stack.pop() != cleanStr[i]:
                    return False
            else:
                stack.append(cleanStr[i])

        return True
