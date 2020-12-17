package Easy.RemoveDuplicatesFromSortedList;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class Solution {

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode current = head;
        ListNode next = head.next;
        while (next != null) {
            if (current.val == next.val) {
                // remove duplicate
                current.next = next.next;
                next = current.next;
            } else {
                current = current.next;
                next = next.next;
            }
        }
        return head;
    }
    
}