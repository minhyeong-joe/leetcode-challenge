package Easy.AddToArrayFormInteger;

import java.util.Arrays;

public class Driver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] A = {1, 2};
        int K = 298;
        System.out.println("Input: A = " + Arrays.toString(A) + ", K = " + K );
        System.out.println("Output: " + sol.addToArrayForm(A, K).toString());    
    }

}