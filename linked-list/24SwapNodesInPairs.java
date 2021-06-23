public class SwapNodesInPairs {
    class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode prev = dummy;
        while(head != null && head.next != null) {
            ListNode first = head, second = head.next, next = second.next;
            prev.next = second;
            second.next = first;
            first.next = next;
            
            prev = first;
            head = first.next;
        }
        return dummy.next;
    }

    public ListNode recursive(ListNode head) {
        if(head != null || head.next != null) return head;
        ListNode first = head, second = head.next;
        first.next = recursive(second.next);
        second.next = first;
        return second;
    }
}
