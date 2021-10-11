'''
Given a linked list, reverse the nodes of a linked list k at a 
time and return its modified list.

k is a positive integer and is less than or equal to the 
length of the linked list. If the number of nodes is not a 
multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes 
themselves may be changed.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # reverse
        def reverse(head, k):
            prev = None
            curr_node = head
            while k > 0:
                next_node = curr_node.next
                curr_node.next = prev
                prev = curr_node
                curr_node = next_node
                k -= 1
            return prev
            
        curr = head
        new_head = None
        ktail = None
        
        while curr:
            n = k
            curr = head
            while curr and n > 0:
                curr = curr.next
                n -= 1

            if n > 0:
                break

            rev_head = reverse(head, k)
            if not new_head:
                new_head = rev_head

            if ktail:
                ktail.next = rev_head
                
            ktail = head
            head = curr
        
        if ktail:
            ktail.next = head
        return new_head if new_head else head