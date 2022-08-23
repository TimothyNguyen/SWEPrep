# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for l in lists:
            if l:
                head = l
                while head:
                    heapq.heappush(min_heap, head.val)
                    head = head.next
        head, tail = None, None
        while min_heap:
            temp = ListNode(heapq.heappop(min_heap))
            if tail is None:
                head = temp
            else:
                tail.next = temp
            tail = temp
        return head
