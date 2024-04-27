# Longest Palindrome

DS: Dictionary

- Understand that constructing the longest palindrome can be made by all even-lengthed characters and 1 odd-lenghted character
- Count up all the characters in the strings and record their counts in a dictionary with key storing each character and value storing how many times it shows up in the string
- Afterwards, add up all the even-lengthed characters and odd-lengthed characters (-1 to make them even)
- If there was an odd-lengthed character, incrememnt the value to account for one odd-lengthed character allowed in the final palindrome
