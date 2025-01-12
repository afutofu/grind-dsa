from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        head = None
        curr = None

        while list1 != None and list2 != None:
            if curr == None:
                if list1.val < list2.val:
                    curr = list1
                    list1 = list1.next
                else:
                    curr = list2
                    list2 = list2.next

                head = curr
                continue

            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1 == None:
            curr.next = list2
        elif list2 == None:
            curr.next = list1

        # print(list1, list2, curr)

        return head


if __name__ == "__main__":
    s = Solution()

    # Example 1
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    mergedList = s.mergeTwoLists(list1, list2)
    while mergedList != None:
        print(mergedList.val)
        mergedList = mergedList.next

    # Example 2
    list1 = None
    list2 = None
    mergedList = s.mergeTwoLists(list1, list2)
    assert mergedList == None

    # Example 3
    list1 = None
    list2 = ListNode(0)
    mergedList = s.mergeTwoLists(list1, list2)
    while mergedList != None:
        print(mergedList.val)
        mergedList = mergedList.next
