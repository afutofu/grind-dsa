# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Edge case, LL with l <= 2
        if head.next == None:
            return
        if head.next.next == None:
            return

        midNode = fast = head
        while fast and fast.next:
            nextFast = fast.next.next
            if nextFast == None or nextFast.next == None:
                temp = midNode.next
                midNode.next = None
                midNode = temp
            else:
                midNode = midNode.next
            fast = nextFast

        l1 = head
        l2 = midNode

        # Reverse l2
        prev = None
        curr = l2
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l2 = prev

        # p1 = l1
        # p2 = l2

        # while p1 != None:
        #     print(p1.val)
        #     p1 = p1.next

        # while p2 != None:
        #     print(p2.val)
        #     p2 = p2.next

        # print()

        curr = head
        nextNode = l2
        while nextNode != None:
            # print(curr.val)
            temp = curr.next
            curr.next = nextNode
            nextNode = temp

            curr = curr.next

        return None


if __name__ == "__main__":
    s = Solution()

    # Example 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    s.reorderList(head)
    while head != None:
        print(head.val)
        head = head.next

    # Example 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s.reorderList(head)
    while head != None:
        print(head.val)
        head = head.next

    # Example 3
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    s.reorderList(head)
    while head != None:
        print(head.val)
        head = head.next

    # Example 4
    head = ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))
    )
    s.reorderList(head)
    while head != None:
        print(head.val)
        head = head.next
