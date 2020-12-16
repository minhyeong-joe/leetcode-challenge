package Easy.MaxProductofThreeNumbers;

import java.util.Arrays;

public class TestDriver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] input1 = {1,2,3};
        System.out.println("Input: " + Arrays.toString(input1));
        System.out.println("Output: " + sol.maximumProduct(input1));
        System.out.println();

        int[] input2 = {3,4,2,1};
        System.out.println("Input: " + Arrays.toString(input2));
        System.out.println("Output: " + sol.maximumProduct(input2));
        System.out.println();

        int[] input3 = {3, 2, -4, -5, 4};
        System.out.println("Input: " + Arrays.toString(input3));
        System.out.println("Output: " + sol.maximumProduct(input3));
        System.out.println();
    }

}