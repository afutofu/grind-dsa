# Linked List Cycle

DS: Linked List
Use: Two pointers

- Initialize two pointers, walker and runner to be the head of the linked list. These two pointers will traverse the linked list.
- While loop with the condition that runner's next node and runner's next's next node is not None
- In the loop, walker will traverse one node at a time and runner will traverse two nodes at a time
- If there is a cycle, there will come a point when walker and runner will be the same node, at which point return True
- Else if the loop exists because runner has reached the end of the linked list (and thus no cycle is found), return False
