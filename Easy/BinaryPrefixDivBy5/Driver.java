package Easy.BinaryPrefixDivBy5;

import java.util.Arrays;

public class Driver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] input = {0,1,1,1,1,1};
        System.out.println("Input: " + Arrays.toString(input));
        System.out.println("Output: " + sol.prefixesDivBy5(input).toString());    
    }

}