class Solution {

    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null) return true;
        ListNode l1 = head; // Head of first half
        ListNode slow = head; // Head of second half
        ListNode fast = head; // Tail of second half
        ListNode prev = null; // Tail of first half
        while(fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        } 
        prev.next = null;
        // Reverse 2nd half
        ListNode l2 = reverse(slow);
        
        while(l1 != null) {
            if(l1.val != l2.val) return false;
            l1 = l1.next;
            l2 = l2.next;
        }
        return true;
    }
    
    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while(curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}