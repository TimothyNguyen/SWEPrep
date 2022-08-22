# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Time: O(n), Space: O(1)
'''
For cyclic lists, hare and tortoise will point to the same node after F+C-h iterations, 
as demonstrated in the proof of correctness. F+C-h ≤F+C=n, so phase 1 runs in O(n) time. Phase 2 runs for F < n
iterations, so it also runs in O(n) time.

For acyclic lists, hare will reach the end of the list in roughly n/2 iterations, causing the function to return before phase 2. Therefore, regardless of which category of list the algorithm receives, it runs in time linearly proportional to the number of nodes.
'''
class Solution:
    def getIntersect(self, head):
        slow = head
        fast = head
            
        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        intersect = self.getIntersect(head)
        if not intersect:
            return None
        
        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1