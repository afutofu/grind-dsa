# Flood Fill

Tech: DFS and recursion

- Make sure that the targeted element is not the same color as the color argument
- Use a helper recursive function which takes in an extra argument which stores the current element
- Helper function base cases are (1) if the given indexes are not within the boundary of the matrix and (2) the value given by the indexes is not the same as the value of the color
- Else, recursively call the helper function four times in the +1 and -1 x and y axis
