package Medium.ReverseLinkedList2;

import Medium.ReverseLinkedList2.Solution.ListNode;

public class Driver {

    public static void main(String[] args) {
        Solution sol = new Solution();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.println(head);
        int m = 2;
        int n = 4;
        head = sol.reverseBetween(head, m, n);
        System.out.println(head);
    }
}
