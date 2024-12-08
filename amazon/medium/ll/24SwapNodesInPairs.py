# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n1, n2 = head, head.next
        head = n2
        while n1 and n2:
            next_node = n2.next
            n2.next = n1
            if next_node and next_node.next:
                n1.next = next_node.next
                n1 = next_node
                n2 = next_node.next
            elif next_node:
                n1.next = next_node
                break
            else:
                n1.next = None
                break
        return head

