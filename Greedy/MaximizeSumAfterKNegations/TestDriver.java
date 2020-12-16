package Easy.MaximizeSumAfterKNegations;

import java.util.Arrays;

public class TestDriver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        int[] input1 = {4,2,3};
        int k1 = 1;
        System.out.println("Input: A= " + Arrays.toString(input1) + ", K = " + k1);
        System.out.println("Output: " + sol.largestSumAfterKNegations(input1, k1));
        System.out.println();
        
        int[] input2 = {3,-1,0,2};
        int k2 = 3;
        System.out.println("Input: A= " + Arrays.toString(input2) + ", K = " + k2);
        System.out.println("Output: " + sol.largestSumAfterKNegations(input2, k2));
        System.out.println();
        
        int[] input3 = {2,-3,-1,5,-4};
        int k3 = 2;
        System.out.println("Input: A= " + Arrays.toString(input3) + ", K = " + k3);
        System.out.println("Output: " + sol.largestSumAfterKNegations(input3, k3));
    }
}