package Medium.LinkedListCycle2;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

/**
 * Solution
 * Use the hare and tortoise algorithm to detect cycle
 */
public class Solution {

    public ListNode detectCycle(ListNode head) {
        // empty list
        if (head == null) {
            return null;
        }
        ListNode hare = head;
        ListNode tortoise = head;
        do {
            tortoise = tortoise.next;
            // hare moves twice as fast as tortoise
            hare = hare.next;
            // if gets to the end of list (null), then no cycle
            if (hare == null) {
                return null;
            }
            hare = hare.next;
            if (hare == null) {
                return null;
            }
        } while (hare != tortoise);
        // System.out.println("First met at (value): " + hare.val);
        // return the tortoise to the beginning and move both hare and tortoise one step at a time
        tortoise = head;
        while (hare != tortoise) {
            tortoise = tortoise.next;
            hare = hare.next;
        }
        // System.out.println("Cycle starts at (value): " + tortoise.val);
        // the second time they meet is the entry point of the cycle (return either tortoise or hare)
        return tortoise;
    }
    
}