from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, linked_list: Optional[ListNode]) -> Optional[ListNode]:
        if not linked_list:
            return linked_list

        current = linked_list
        while current.next:
            next_node = current.next
            if current.val == next_node.val:
                current.next = next_node.next
            else:
                current = current.next
        return linked_list
