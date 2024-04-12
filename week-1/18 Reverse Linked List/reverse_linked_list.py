# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        stack = []

        # Go through the linked list, store unlink each node to prevent a cycle,
        # and store each node in a stack
        curr = head
        while curr != None:
            stack.append(curr)
            next_node = curr.next
            curr.next = None
            curr = next_node

        # Get the new head of the node, iterate through the stack's node,
        # and link each node to the next
        new_head = stack.pop()
        curr = new_head
        while len(stack) > 0:
            curr.next = stack.pop()
            curr = curr.next

        # Return the new head
        return new_head
