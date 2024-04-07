class Solution:
    def isValid(self, s: str) -> bool:

        # Use stack to store opening parenthesis
        openStack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                openStack.append(char)
            else:
                if len(openStack) == 0:
                    return False

                latestOpen = openStack.pop()
                if (
                    char == ")"
                    and latestOpen != "("
                    or char == "}"
                    and latestOpen != "{"
                    or char == "]"
                    and latestOpen != "["
                ):
                    return False

        if len(openStack) > 0:
            return False
        else:
            return True
