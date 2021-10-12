class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Time: O(n), O(1) space
        def reverse(node):
            prev = None
            curr = node
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        if not head:
            return True
        
        # Find the first half and second half
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        reverse_head = reverse(slow.next)

        curr = head
        while curr and reverse_head:
            if curr.val != reverse_head.val:
                return False
            curr = curr.next
            reverse_head = reverse_head.next
        return True

        # 1 - 2 
        # 2 - 1