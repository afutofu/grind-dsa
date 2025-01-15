from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # n == 0
        if head == None:
            return None

        # n == 1
        if head.next == None:
            return Node(head.val, None, head.random)

        # n >= 2
        newHead = Node(head.val, None, None)

        curr1 = newHead
        curr2 = head.next

        m = {head: newHead}

        # Create shallow copies (no random node assigned)
        while curr2 != None:
            newNode = Node(curr2.val)
            curr1.next = newNode

            m[curr2] = newNode

            curr1 = curr1.next
            curr2 = curr2.next

        # Assign random node to each
        curr1 = newHead
        curr2 = head

        while curr2 != None:
            if curr2.random != None:
                curr1.random = m[curr2.random]

            curr1 = curr1.next
            curr2 = curr2.next

        return newHead


if __name__ == "__main__":
    s = Solution()

    # Example 1
    head = Node(7)
    head.next = Node(13)
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(1)
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head
    newHead = s.copyRandomList(head)
    assert newHead.val == 7
    assert newHead.next.val == 13
    assert newHead.next.next.val == 11
    assert newHead.next.next.next.val == 10
    assert newHead.next.next.next.next.val == 1
    assert newHead.random == None
    assert newHead.next.random.val == 7
    assert newHead.next.next.random.val == 1
    assert newHead.next.next.next.random.val == 11
    assert newHead.next.next.next.next.random.val == 7

    # Example 2
    head = Node(1)
    head.next = Node(2)
    head.random = head.next
    head.next.random = head
    newHead = s.copyRandomList(head)
    assert newHead.val == 1
    assert newHead.next.val == 2
    assert newHead.random.val == 2
    assert newHead.next.random.val == 1

    # Example 3
    head = Node(3)
    head.next = Node(3)
    head.next.next = Node(3)
    head.next.random = head
    newHead = s.copyRandomList(head)
    assert newHead.val == 3
    assert newHead.next.val == 3
    assert newHead.next.next.val == 3
    assert newHead.next.random.val == 3

    # Example 4
    head = None
    newHead = s.copyRandomList(head)
    assert newHead == None
