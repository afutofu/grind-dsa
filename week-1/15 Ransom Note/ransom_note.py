class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # If ransomNote is longer than magazine, then magazine is unable to construct ransomNote
        if len(ransomNote) > len(magazine):
            return False

        # Convert strings to character lists
        magList = [char for char in magazine]
        ranList = [char for char in ransomNote]

        # Make alphabet counter using an array of 26 indexes for each letter
        alphabet_counter = [0] * 26

        # Add up counter from magazine
        for c in magList:
            index = ord(c) - ord("a")
            alphabet_counter[index] += 1

        # Decrement counter by matching letters to construct ransomNote
        for c in ransomNote:
            index = ord(c) - ord("a")
            alphabet_counter[index] -= 1
            if alphabet_counter[index] < 0:
                return False

        return True
