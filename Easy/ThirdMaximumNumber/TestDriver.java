package Easy.ThirdMaximumNumber;

import java.util.Arrays;

public class TestDriver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] input1 = {3,2,1};
        System.out.println("Input: " + Arrays.toString(input1));
        System.out.println("Output: " + sol.thirdMax(input1));

        System.out.println();

        int[] input2 = {1,2};
        System.out.println("Input: " + Arrays.toString(input2));
        System.out.println("Output: " + sol.thirdMax(input2));

        System.out.println();
        
        int[] input3 = {2,2,3,1};
        System.out.println("Input: " + Arrays.toString(input3));
        System.out.println("Output: " + sol.thirdMax(input3));

        System.out.println();
        int[] input4 = {1,1,2};
        System.out.println("Input: " + Arrays.toString(input4));
        System.out.println("Output: " + sol.thirdMax(input4));
    }

}