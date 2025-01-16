from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        p1 = l1
        p2 = l2
        carry = 0
        while p1 != None or p2 != None:
            v1 = 0
            v2 = 0

            if p1 != None:
                v1 = p1.val

            if p2 != None:
                v2 = p2.val

            cSum = v1 + v2 + carry

            if carry == 1:
                carry = 0

            if cSum >= 10:
                carry = 1
                p1.val = cSum - 10
            else:
                p1.val = cSum

            # print(v1, v2, carry, cSum)

            if (
                p1.next == None
                and (p2 == None or (p2 != None and p2.next == None))
                and carry == 1
            ):
                p1.next = ListNode(1)
                break
            elif p1.next == None and p2 != None and p2.next != None:
                p1.next = p2.next
                p2.next = None

            p1 = p1.next

            if p2 != None:
                p2 = p2.next

        return l1


if __name__ == "__main__":
    s = Solution()

    # Example 1
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s.addTwoNumbers(l1, l2)
    # Expected: 7 -> 0 -> 8
    # Explanation: 342 + 465 = 807.
    # Output: 7 -> 0 -> 8
    # print(s.addTwoNumbers(l1, l2))
    print(s.addTwoNumbers(l1, l2).val)
    print(s.addTwoNumbers(l1, l2).next.val)
    print(s.addTwoNumbers(l1, l2).next.next.val)
    print(s.addTwoNumbers(l1, l2).next.next.next)
    print(s.addTwoNumbers(l1, l2).next.next.next.next)
