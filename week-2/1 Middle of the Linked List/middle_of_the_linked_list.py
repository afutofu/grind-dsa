# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Store all nodes in a list
        node_list = []

        # Traverse the linked list and store all nodes in the list
        curr = head
        while curr != None:
            node_list.append(curr)
            curr = curr.next

        # Return the middle node
        return node_list[len(node_list) // 2]
