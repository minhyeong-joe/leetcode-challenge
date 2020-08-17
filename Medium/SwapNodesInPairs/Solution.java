package Medium.SwapNodesInPairs;


// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}


/**
 * Key is to constantly keep track of prev, current, and next nodes to effectively swap orders in single run
 * start current with the second node (if 0 or 1 element simply return original head)
 * swapping prev and curr is straightforward; cur.next = prev
 * but prev.next can be next node or next's next node
 * 1. prev.next = next if next.next does not exist
 * 2. prev.next = next.next if next.next exists
 * Move prev, current, next one node to right at a time until current node is null
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode prev = head;
        if (head == null || head.next == null) {
            return head;
        }
        ListNode cur = prev.next;
        head = cur;
        ListNode next;
        ListNode nextPrev;
        while (cur != null) {
            next = cur.next;
            // keep next in nextPrev as it will be used as next iteration's prev, but will be disconnect with this swap
            nextPrev = next;
            cur.next = prev;
            if (next == null || next.next == null) {
                prev.next = next;
            } else {
                prev.next = next.next;
            }
            // if next has next, then current is next.next
            // ie) 1->2->3->4->5->6, after one swap, current is 4, prev is 3, next is 5 in 2->1->4, 3->4->5->6
            if (next == null) {
                cur = next;
            } else {
                cur = next.next;
            }
            prev = nextPrev;
        }
        return head;
    }
}