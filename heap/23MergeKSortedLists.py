# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for l in lists:
            if l:
                head = l
                while head:
                    heapq.heappush(pq, head.val)
                    head = head.next
        head = None
        tail = None
        while len(pq) > 0:
            temp = ListNode(heapq.heappop(pq))
            if tail is None: 
                head = temp
            else: 
                tail.next = temp
            tail = temp
        return head

