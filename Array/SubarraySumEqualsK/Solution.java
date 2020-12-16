package Medium.SubarraySumEqualsK;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int subarraySum(int[] nums, int k) {
        int numSubarray = 0;
        int cumSum = 0;
        // hashmap to keep track of cumulative sums
        Map<Integer, Integer> sumCount = new HashMap<>();
        sumCount.put(0,1);
        for (int num: nums) {
            cumSum += num;
            // if cumSum-k appeared in Map, then add count
            if (sumCount.containsKey(cumSum-k)) {
                numSubarray += sumCount.get(cumSum-k);
            }
            // count cumulative sum
            if (!sumCount.containsKey(cumSum)) {
                sumCount.put(cumSum, 1);
            } else {
                sumCount.put(cumSum, sumCount.get(cumSum)+1);
            }
        }
        return numSubarray;
    }
}