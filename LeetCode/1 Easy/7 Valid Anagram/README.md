# Valid Anagram

DS: List

- First check if the the two strings are the same length, return false if not
- Create a letters list to store all the characters of the first string
- Iterate through each character in the second string. If the character exists in the letters list, remove it from the list, and if it doesn't exist in the list, return false
- Finally, check if the length of the list is 0 and return true, else return false (meaning the first list had more of a certain character(s) than the second)
