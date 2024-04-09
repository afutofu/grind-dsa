# Binary Search

Used: Binary Search

- Setup low and high variables to store get low and high index of sorted list
- Setup while loop with the condition that low is lesser than or equals to high
- Within the while loop, calculate the midpoint of the current list by averaging out low and high values
- Using this midpoint, check if the target is in the list location with midpoint index. If it is, return the midpoint (as it is the index)
- If the target is lesser than the element at the midpoint index, increment the low variable and continue the loop
- If the target is greater than the leemnt at the midpoint index, decrement the high variable and continue the loop
- The low and high variable will change until it reaches the termination condition of the while loop, unless the target is found
- If the while loop exists, that means the target is not found and thus return -1
