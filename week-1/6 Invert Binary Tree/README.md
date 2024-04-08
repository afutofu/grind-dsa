# Merge Two Sorted Lists

DS: Binary Tree

- Traverse the binary tree using a recursive function
- Base case is if current root is not null
- If the root is not null, recursively call the function with the root's left child and again with the root's right child
- After recursively calling and obtaining the root's left and right child, swap them
- Return the root after swapping
