# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        max_heap = []
        for curr_node in lists:
            while curr_node:
                heapq.heappush(max_heap, curr_node.val)
                curr_node = curr_node.next

        head = ListNode(-1)
        tail = head
        while max_heap:
            num = heapq.heappop(max_heap)
            tail.next = ListNode(num)
            tail = tail.next
        return head.next