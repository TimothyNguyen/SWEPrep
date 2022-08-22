import heapq
from tkinter import E

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for l in lists:
            if l:
                head = l
                while head:
                    heapq.heappush((head.val, head))
                    head = head.next
        
        head, tail = None, None
        while heap:
            _, node = heapq.heappop()
            if not head:
                head = node
            else:
                tail.next = node 
            tail = node
        return head