package Medium.LinkedListCycle2;

import java.util.Arrays;

public class TestDriver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int i = 0;
        
        int[] arr1 = {3,2,0,-4};
        int pos1 = 1;
        ListNode head1 = createLinkedList(arr1, pos1);
        System.out.println("Input: head = " + Arrays.toString(arr1) + ", pos = " + pos1);
        ListNode cycleEntry1 = sol.detectCycle(head1);
        if (cycleEntry1 == null) {
            System.out.println("Output: no cycle");
        } else {
            while (head1 != cycleEntry1) {
                i++;
                head1 = head1.next;
            }
            System.out.println("Output: tail connects to node index " + i);
        }
        System.out.println();
        
        i = 0;
        int[] arr2 = {1,2};
        int pos2 = 0;
        ListNode head2 = createLinkedList(arr2, pos2);
        System.out.println("Input: head = " + Arrays.toString(arr2) + ", pos = " + pos2);
        ListNode cycleEntry2 = sol.detectCycle(head2);
        if (cycleEntry2 == null) {
            System.out.println("Output: no cycle");
        } else {
            while (head2 != cycleEntry2) {
                i++;
                head2 = head2.next;
            }
            System.out.println("Output: tail connects to node index " + i);
        }
        System.out.println();
        
        int[] arr3 = {1};
        int pos3 = -1;
        ListNode head3 = createLinkedList(arr3, pos3);
        System.out.println("Input: head = " + Arrays.toString(arr3) + ", pos = " + pos3);
        ListNode cycleEntry3 = sol.detectCycle(head3);
        if (cycleEntry3 == null) {
            System.out.println("Output: no cycle");
        } else {
            while (head3 != cycleEntry3) {
                i++;
                head3 = head3.next;
            }
            System.out.println("Output: tail connects to node index " + i);
        }
        System.out.println();
    }

    // helper to construct list from input array and pos
    // returns the head node
    public static ListNode createLinkedList(int[] arr, int pos) {
        ListNode head = new ListNode(arr[0]);
        ListNode temp = head;
        for (int i = 1; i < arr.length; i++) { 
            ListNode newNode = new ListNode(arr[i]);
            temp.next = newNode;
            temp = newNode;
        }
        if (pos >= 0) {
            // find the node where cycle begins
            ListNode iter = head;
            for (int i = 0; i < pos; i++) {
                iter = iter.next;
            }
            // temp is pointing to the last node in the list
            temp.next = iter;
        }
        return head;
    }
}