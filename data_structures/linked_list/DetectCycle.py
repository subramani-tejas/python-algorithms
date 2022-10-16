# leetcode 141/142
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not self.has_cycle(head):
            return

        cycle_length = self.get_cycle_length(head=head)
        x = head
        y = head

        while cycle_length > 0:
            y = y.next
            cycle_length -= 1

        while x != y:
            x = x.next
            y = y.next

        return x

    def get_cycle_length(self, head):
        x = head
        y = head

        while y and y.next:
            x = x.next
            y = y.next.next
            if x == y:
                break

        x = x.next
        length = 1

        while x != y:
            x = x.next
            length += 1

        return length

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        x = head
        y = head

        while y and y.next:
            x = x.next
            y = y.next.next

            if x == y:
                return True

        return False


