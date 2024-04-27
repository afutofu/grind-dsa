class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        letter_counter = {}

        # Build up letter counter
        for letter in s:
            if letter in letter_counter:
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 1

        # Add up even-length letters and find the longest length odd letter
        even_letters_length = 0
        odd_letters_length = 0
        odd_letters_count = 0
        for letter in letter_counter:
            letter_count = letter_counter[letter]
            if letter_count % 2 == 0:
                even_letters_length += letter_count
            else:
                odd_letters_count += 1
                odd_letters_length += letter_count - 1

        # Add them both
        total_length = odd_letters_length + even_letters_length
        if odd_letters_count >= 1:
            total_length += 1

        return total_length
