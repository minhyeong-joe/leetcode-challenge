package Easy.FairCandySwap;

import java.util.HashSet;
import java.util.Set;

/**
 * Solution
 */
public class Solution {

    public int[] fairCandySwap(int[] A, int[] B) {
        int sumA = 0, 
            sumB = 0;
        // make array B into set for faster search
        Set<Integer> setB = new HashSet<>();
        for (int v: A) {
            sumA += v;
        }
        for (int v: B) {
            sumB += v;
            setB.add(v);
        }
        int goalSum = (sumA + sumB) / 2;
        for (int a: A) {
            int target_b = goalSum - sumA + a;
            if (setB.contains(target_b)) {
                return new int[]{a, target_b};
            }
        }
        return null;
    }

}