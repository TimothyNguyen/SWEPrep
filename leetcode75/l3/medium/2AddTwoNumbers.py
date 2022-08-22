# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        curr = head
        while l1 and l2:
            sum_val = l1.val + l2.val + carry
            curr.next = ListNode(sum_val % 10)
            curr = curr.next
            carry = sum_val // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum_val = l1.val + carry
            curr.next = ListNode(sum_val % 10)
            curr = curr.next
            carry = sum_val // 10
            l1 = l1.next
        
        while l2:
            sum_val = l2.val + carry
            curr.next = ListNode(sum_val % 10)
            curr = curr.next
            carry = sum_val // 10
            l2 = l2.next
        
        if carry > 0:
            curr.next = ListNode(carry)
            
        return head.next