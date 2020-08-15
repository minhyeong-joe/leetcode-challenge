package Easy.N_RepeatedElementInArray;

import java.util.Arrays;

public class TestDriver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] input1 = {1,2,3,3};
        System.out.println("Input: " + Arrays.toString(input1));
        System.out.println("Output: " + sol.repeatedNTimes(input1));
        System.out.println();
        
        int[] input2 = {2,1,2,5,3,2};
        System.out.println("Input: " + Arrays.toString(input2));
        System.out.println("Output: " + sol.repeatedNTimes(input2));
        System.out.println();
        
        int[] input3 = {5,1,5,2,5,3,5,4};
        System.out.println("Input: " + Arrays.toString(input3));
        System.out.println("Output: " + sol.repeatedNTimes(input3));
        System.out.println();
    }

}