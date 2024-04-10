# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        walker = head
        runner = head

        while runner.next != None and runner.next.next != None:
            walker = walker.next
            runner = runner.next.next

            if walker == runner:
                return True

        return False
