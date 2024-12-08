# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: Optional[ListNode]):
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
        head = reverse(head)
        return head

'''
1 -> 2 -> 3 -> 4 -> 5
1 -> 2 <- 3
'''