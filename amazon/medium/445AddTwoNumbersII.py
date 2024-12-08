# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_ll(node: Optional[ListNode]):
            prev_node = None
            while node:
                if not node:
                    return node
                if not node.next:
                    node.next = prev_node
                    return node
                next_node = node.next
                node.next = prev_node
                prev_node = node
                node = next_node

        l1 = reverse_ll(l1)
        l2 = reverse_ll(l2)

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
        true_head = dummy_head.next
        return reverse_ll(true_head)