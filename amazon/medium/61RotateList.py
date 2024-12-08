# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        len_ll = 0
        curr_node = head
        old_tail = None
        while curr_node.next:
            len_ll += 1
            curr_node = curr_node.next
            old_tail = curr_node
        
        k = k % len_ll
        if k == 0:
            return head
        new_tail_count = len_ll - k - 2
        old_head = head
        curr_node = head
        while curr_node:
            if new_tail_count == 0:
                break
            curr_node = curr_node.next
            new_tail_count -= 1
        new_tail = curr_node
        new_head = curr_node.next
        new_tail.next = None
        old_tail.next = head
        return new_head
        
        