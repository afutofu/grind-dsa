# Valid Parentheses

DS: Stack

- Use stack to store opening parentheses
- Iterate over every character in string s
- If char is an opening parenthesis, store in stack
- If not an opening parenthesis, check if stack is empty, if so then return False
- If stack not empty, pop the last value of the stack to get the latest opening parenthesis
- If opening parenthesis doesn't match closing parenthesis, return False
- Finally, check if any unused open parenthesis
- If there are any, return False, else return True
