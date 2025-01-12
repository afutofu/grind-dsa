# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Initialize mergedNode
        mergedListNode = ListNode()
        trackerNode = mergedListNode

        # While both lists are not empty
        while list1 != None and list2 != None:

            if list1.val < list2.val:
                trackerNode.next = list1
                list1 = list1.next
            else:
                trackerNode.next = list2
                list2 = list2.next

            trackerNode = trackerNode.next

        # If list1 is not empty and list2 is empty
        if list1 != None:
            trackerNode.next = list1

        #  If list2 is not empty
        else:
            trackerNode.next = list2

        # Return the next value of mergedListNode (because the first value is 0 and only used as an initializer
        return mergedListNode.next
