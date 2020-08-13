package Medium.MaximumLengthPairChain;

import java.util.Arrays;

public class TestDriver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] input1 = {{1,2}, {2,3}, {3,4}};
        System.out.println("Input: " + Arrays.deepToString(input1));
        System.out.println("Output: " + sol.findLongestChain(input1));
        System.out.println();

        int[][] input2 = {{-6,9},{1,6},{8,10},{-1,4},{-6,-2},{-9,8},{-5,3},{0,3}};
        System.out.println("Input: " + Arrays.deepToString(input2));
        System.out.println("Output: " + sol.findLongestChain(input2));
        System.out.println();
    }
}