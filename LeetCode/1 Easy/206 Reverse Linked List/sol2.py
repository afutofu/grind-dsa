from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        prev = head
        curr = head.next
        prev.next = None
        while curr.next != None:
            # print(curr.val)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr.next = prev

        return curr


if __name__ == "__main__":
    s = Solution()

    # Example 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    newHead = s.reverseList(head)
    for i in range(5):
        assert newHead.val == 5 - i
        newHead = newHead.next

    # Example 2
    head = ListNode(1, ListNode(2))
    newHead = s.reverseList(head)
    for i in range(2):
        assert newHead.val == 2 - i
        newHead = newHead.next

    # Example 3
    head = ListNode(1)
    newHead = s.reverseList(head)
    # print(newHead.val)
    assert newHead.val == 1
    newHead = newHead.next

    # Example 4
    head = None
    newHead = s.reverseList(head)
    assert newHead == None

    # Example 5
    head = ListNode(1, ListNode(2, ListNode(3)))
    newHead = s.reverseList(head)
    for i in range(3):
        assert newHead.val == 3 - i
        newHead = newHead.next

    print("Passed all test cases!")
