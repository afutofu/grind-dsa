from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None and n == 1:
            return None
        if head.next == None and n > 1:
            return head

        # Get length of list
        l = 0
        p1 = head
        while p1 != None:
            l += 1
            p1 = p1.next

        if n > l:
            n = n % l

        p2 = head
        prev = None
        c = 0
        while c <= l:
            if c == l - n:
                if prev == None:
                    # Meaning first item in the list
                    head = p2.next
                else:
                    prev.next = p2.next
                break

            prev = p2
            p2 = p2.next
            c += 1

        return head


if __name__ == "__main__":
    s = Solution()

    # Example 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    newHead = s.removeNthFromEnd(head, n)
    assert newHead.val == 1
    assert newHead.next.val == 2
    assert newHead.next.next.val == 3
    assert newHead.next.next.next.val == 5

    # Example 2
    head = ListNode(1)
    n = 1
    newHead = s.removeNthFromEnd(head, n)
    assert newHead == None

    # Example 3
    head = ListNode(1, ListNode(2))
    n = 1
    newHead = s.removeNthFromEnd(head, n)
    assert newHead.val == 1
    assert newHead.next == None

    # Example 4
    head = ListNode(1, ListNode(2))
    n = 2
    newHead = s.removeNthFromEnd(head, n)
    assert newHead.val == 2
    assert newHead.next == None

    # Example 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 5
    newHead = s.removeNthFromEnd(head, n)
    assert newHead.val == 2
    assert newHead.next.val == 3
    assert newHead.next.next.val == 4
    assert newHead.next.next.next.val == 5
