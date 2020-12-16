package Medium.ReverseLinkedList2;

public class Solution {

    // Definition for singly-linked list.
    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }

        // helper method to print out in string form
        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            ListNode head = this;
            while (head != null) {
                sb.append(head.val + "->");
                head = head.next;
            }
            sb.append("NULL");

            return sb.toString();
        }
    }

    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m == n) {
            return head;
        }
        ListNode cur, prev, next, breakpoint;
        int numSwaps = 0;
        // first move cur to m-th node in list
        cur = head;
        breakpoint = head;
        // cursor and breakpoint can be at the same location if m == 1
        for (int i = 0; i < m - 1; i++) {
            cur = cur.next;
        }
        for (int i = 0; i < m - 2; i++) {
            breakpoint = breakpoint.next;
        }
        prev = breakpoint;
        next = cur.next;
        // needs n-m swaps
        while (numSwaps < n - m) {
            // shift all pointers
            prev = cur;
            cur = next;
            next = next.next;
            // reverse
            cur.next = prev;
            numSwaps++;
        }
        // outer reversal patch-ups
        // if breakpoint is part of inner reversal, then different patching required
        if (m == 1) {
            breakpoint.next = next;
            head = cur;
        } else {
            breakpoint.next.next = next;
            breakpoint.next = cur;
        }

        return head;
    }

}
