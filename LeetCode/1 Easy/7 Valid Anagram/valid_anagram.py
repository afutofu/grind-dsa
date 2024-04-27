class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Create a list of letters
        letters = []

        # Go through the first string s and put each character in the list
        for letter in s:
            letters.append(letter)

        # Go through the second string t one character at a time
        # and remove values from the letters list if found.
        # If a letter is not found in the list, then return false
        # because it means the second string has more of a certain letter(s) than the first string.
        for letter in t:
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        # If letters list is empty, then return true,
        # else return false because it means the first string
        # has more of a certain letter(s) than the second.
        if len(letters) == 0:
            return True
        else:
            return False
