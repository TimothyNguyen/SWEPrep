/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        int count = 0;
        ListNode curr = head;
        while(count < k && curr != null) {
            curr = curr.next;
            count++;
        }
        if(count == k) {
            ListNode new_node = reverse(head, k);
            head.next = reverseKGroup(curr, k);
            return new_node;
        }
        return head;
    }
    
    private ListNode reverse(ListNode head, int k) {
        ListNode new_head = null;
        ListNode ptr = head;
        while(k > 0) {
            ListNode next = ptr.next;
            ptr.next = new_head;
            new_head = ptr;
            ptr = next;
            k--;
        }
        return new_head;
    }
}