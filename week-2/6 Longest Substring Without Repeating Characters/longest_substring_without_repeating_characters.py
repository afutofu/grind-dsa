class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_length = 1
        count = 1
        repeat_index = -1

        # Iterate through each character
        for i in range(1, len(s)):

            # Check if previous characters in the substring is repeated
            for j in range(i - 1, repeat_index, -1):

                # If character repeated,
                # set count starting from the index after the cutoff point,
                # Set a new repeat_index
                if s[j] == s[i]:
                    count = i - j - 1
                    repeat_index = j
                    break

            count += 1
            max_length = max(count, max_length)

        return max_length
