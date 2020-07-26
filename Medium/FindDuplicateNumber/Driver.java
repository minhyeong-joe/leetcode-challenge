package Medium.FindDuplicateNumber;

import java.util.Arrays;

public class Driver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] arr = {1,3,4,2,2};
        System.out.println("Input: " + Arrays.toString(arr));
        int dup = sol.findDuplicate(arr);
        System.out.println("Output: " + dup);

        System.out.println();
        int[] arr2 = {3,1,3,4,2};
        System.out.println("Input: " + Arrays.toString(arr2));
        int dup2 = sol.findDuplicate(arr2);
        System.out.println("Output: " + dup2);
    }
}