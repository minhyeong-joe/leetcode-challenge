package Easy.FindLuckyIntegerInArray;

import java.util.Arrays;

public class TestDriver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] arr1 = {2, 2, 3, 4};
        System.out.println("Input: arr = " + Arrays.toString(arr1));
        System.out.println("Output: " + sol.findLucky(arr1));
        System.out.println();

        int[] arr2 = {1,2,2,3,3,3};
        System.out.println("Input: arr = " + Arrays.toString(arr2));
        System.out.println("Output: " + sol.findLucky(arr2));
        System.out.println();

        int[] arr3 = {2, 2, 2, 3, 3};
        System.out.println("Input: arr = " + Arrays.toString(arr3));
        System.out.println("Output: " + sol.findLucky(arr3));
        System.out.println();

        int[] arr4 = {5};
        System.out.println("Input: arr = " + Arrays.toString(arr4));
        System.out.println("Output: " + sol.findLucky(arr4));
        System.out.println();

        int[] arr5 = {7, 7, 7, 7, 7, 7, 7};
        System.out.println("Input: arr = " + Arrays.toString(arr5));
        System.out.println("Output: " + sol.findLucky(arr5));
        System.out.println();
    }
}