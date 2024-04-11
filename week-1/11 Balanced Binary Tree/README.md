# Balanced Binary Tree

DS: Binary Tree

- If the input root is none, return true
- Create a helper recursive function that returns -1 if tree is unbalanced else returns the difference in depth between the subtrees
- Call this function to check if the return output is not equals to -1
- In the helper function, return 0 if the root is none, else recursively call the function on the subtrees
- After calling on subtrees, check if the difference between the output of the subtrees are greater than one, then return -1. And also return -1 if the outputs is -1 (means the tree is unbalanced)
- The -1 condition ensures that once the tree is deemed unbalanced, all the calls back up will see the -1
- After checking this condition, return the max of the left and right subtree height and increment by 1
