# Merge Two Sorted Lists

DS: Linked List

- Initialize merged list (alias merged) node
- Run a while loop while both list1 and list2 have values
- Check if list1 value is lesser than list2 value, set merged's next node to list1 and set list1 node to its next node
- Else if list2 value is lesser than list1 value, do the same thing for list2
- After every iteration, increment the merged node to the next one
- After while loop finishes, if there are still nodes left in either lists, set it as the next node
- Return the next node of merged (first node has incorrect value of 0 because of initialization)
