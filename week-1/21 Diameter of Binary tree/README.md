# Diameter of Binary Tree

Use: Depth-First Search, Recursion

- Get the maximum possible depth of every node recursively
- Whenever we get the depth from both the left and right subtree of the node, compare it to the class variable diameter
- When returning, return the max of the left and the right depth added with 1 to account of that node existing
