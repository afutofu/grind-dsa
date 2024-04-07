# Merge Two Sorted Lists

DS: Linked List

- Initialize dummy list node
- Track the current dummy node
- Run a while loop while both list1 and 2 have values
- Check if list1 is lesser than list2 value, set next node to list1 and increment list1
- Else if list2 value is lesser than list1 value, do the same thing
- After every iteration, increment current node value to the next one
- After while loop finishes, if there are still nodes left in either lists, set it as the next node
- Return the next node of dummy (first node has incorrect value of 0 because of initialization)
