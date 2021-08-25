# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None: return True
        def reverse(head: ListNode):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        prev = None
        l1 = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        l2 = reverse(slow)
        
        while l1:
            if l1.val != l2.val: return False
            l1 = l1.next
            l2 = l2.next
            
        return True