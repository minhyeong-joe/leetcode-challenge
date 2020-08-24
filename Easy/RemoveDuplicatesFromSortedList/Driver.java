package Easy.RemoveDuplicatesFromSortedList;

public class Driver {

    public static void main(String[] args) {
        Solution sol = new Solution();
        // test case: 1 -> 1 -> 1 -> 2 -> 2 -> 3 -> 4 -> 5 -> 5
        ListNode head = new ListNode(1, new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(5)))))))));
        System.out.print("Input: ");
        printList(head);
        
        head = sol.deleteDuplicates(head);
        System.out.print("Output: ");
        printList(head);
    }

    private static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val);
            if (head.next != null) {
                System.out.print(" -> ");
            }
            head = head.next;
        }
        System.out.println();
    }

}