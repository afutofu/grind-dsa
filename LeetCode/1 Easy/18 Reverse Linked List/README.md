# Reverse Linked List

DS: Linked List, Stack

- Initialize a stack
- Iterate through the linked list, unlink them (to avoid a cycle in the next iteration), and store each node in a stack
- Get the new head by popping the top of the stack
- Iterate through the stack by popping each item from the top (effectively reversing the order of the linked list nodes)
- In each iteration, link each node to the next item
- Finally return the new head
