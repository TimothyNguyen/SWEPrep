# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        l, r = head, head.next
        while r:
            while r and l.val == r.val:
                r = r.next
            l.next = r
            next = r
            l = r
            r = next
        if l: l.next = r
        return head