# Lowest Common Ancestor of a Binary Search Tree

DS: Binary Search Tree

- Use a recursive algorithm to solve
- Base case if current root is None, return false
- Check if current root's value is lesser than both of the descendents' values, then recursively call the function passing in the root's right subtree with the same descendents
- Else if the root's value is greater than both of the descendent's values, thenr ecursively call the function passing in the root's left subtree with the same descendents
- Else, this means that the root's value is greater than one of the descendents and lesser than the other, meaning that this is the closest ancestor to both descendents.
