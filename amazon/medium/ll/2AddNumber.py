# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy_head = ListNode()
        tail = dummy_head
        while l1 and l2:
            curr_val = l1.val + l2.val + remainder
            remainder = curr_val // 10
            tail.next = ListNode(curr_val % 10)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curr_val = l1.val + remainder
            remainder = curr_val // 10
            tail.next = ListNode(curr_val % 10)
            tail = tail.next
            l1 = l1.next
        while l2:
            curr_val = l2.val + remainder
            remainder = curr_val // 10
            tail.next = ListNode(curr_val % 10)
            tail = tail.next
            l2 = l2.next
        if remainder > 0:
            tail.next = ListNode(remainder)
        return dummy_head.next