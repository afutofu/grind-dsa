# Valid Palindrome

DS: Stack

- Clean the string with regex and built in methods
- Use a stack and a loop to iterate over the string to add in values in the first half of the string, then compare the second half of the string using popped values in the stack
- Checks if it is an odd length in order to skip the middle character in the string
- If any value does not match the one in the stack, then return False
- If the loop ends, then it is a palindrome
