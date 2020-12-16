package Easy.MaximizeSumAfterKNegations;

import java.util.Arrays;

/**
 * Solution
 */
public class Solution {

    public int largestSumAfterKNegations(int[] A, int K) {
        Arrays.sort(A);
        int sum = 0;
        int i = 0;
        while (K > 0) {
            if (A[i] > A[i+1]) {
                i++;
            }
            A[i] *= -1;
            K--;
        }
        for (int v: A) {
            sum += v;
        }
        return sum;
    }

}