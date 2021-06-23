public class RotateList {
    class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null) return head;
        int n = 1;
        ListNode oldHead = head;
        while(oldHead.next != null) {
            oldHead = oldHead.next;
            n++;
        }

        ListNode new_tail = head, new_head;
        for(int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail.next;
        }
        oldHead.next = head;
        new_head = new_tail.next;
        new_tail.next = null;
        return new_head;
    }

    public ListNode rotateLeft(ListNode head, int k) {
        return null;
    }

}
