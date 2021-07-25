# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        
        def helper(head):
            if not head or not head.next: return head

            flag = False
            while head.next and head.val == head.next.val:
                flag = True
                head = head.next
            if flag: head = helper(head.next)
            else: head.next = helper(head.next)
            return head
        
        return helper(head)