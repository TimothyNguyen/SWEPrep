'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        '''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
# Definition for singly-linked list.
# O(N) time/O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev
        curr, k_tail = head, None
        new_head = None

        while curr:
            n = k
            curr = head
            while curr and n > 0:
                n -= 1
                curr = curr.next
            
            if n > 0:
                break
            
            rev_head = reverse(head, k)
            if not new_head:
                new_head = rev_head

            if k_tail:
                k_tail.next = rev_head
            k_tail = head 
            head = curr   
        
        if k_tail:
            k_tail.next = head
        
        return new_head if new_head else head