package Medium.SwapNodesInPairs;

public class TestDriver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        ListNode head = new ListNode(1, new ListNode (2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
        ListNode iter = head;
        while (iter != null) {
            System.out.print(iter.val);
            if (iter.next != null) {
                System.out.print("->");
            }
            iter = iter.next;
        }
        System.out.println();

        ListNode newHead = sol.swapPairs(head);
        iter = newHead;
        while (iter != null) {
            System.out.print(iter.val);
            if (iter.next != null) {
                System.out.print("->");
            }
            iter = iter.next;
        }
        System.out.println();
    }

}