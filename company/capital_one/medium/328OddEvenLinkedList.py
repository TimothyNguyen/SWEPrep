# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        odd_list = head
        even_list = head.next
        even_list_head = even_list
        while even_list and even_list.next:
            odd_list.next = even_list.next
            odd_list = odd_list.next
            even_list.next = odd_list.next
            even_list = even_list.next
    
        odd_list.next = even_list_head
        return head
    