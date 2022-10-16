# leetcode 21
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x, y = list1, list2

        if x is None:
            return y
        elif y is None:
            return x

        # choose whichever node is smaller to start with
        if x.val <= y.val:
            t = x
            x = x.next
        else:
            t = y
            y = y.next

        # return this head pointer
        ans = t

        # start comparing element by element till one of the heads is None
        while x and y:
            # if x is lesser or equal
            if x.val <= y.val:
                t.next = x
                x = x.next
                t = t.next

            # if y is lesser
            elif x.val > y.val:
                t.next = y
                y = y.next
                t = t.next

        # is x or y is None
        if x is None:
            t.next = y
        elif y is None:
            t.next = x

        return ans
