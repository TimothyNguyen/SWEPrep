// Easy
public class Solution {
    public class ListNode {
        int val;
        ListNode next;

        public ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode currA = headA, currB = headB;
        while(currA != currB) {
            currA = (currA != null) ? currA.next : headB;
            currB = (currB != null) ? currB.next : headA; 
        }
        return currA;
    }
}
