package Medium.MaximumLengthPairChain;

import java.util.Arrays;

class Solution {
    public int findLongestChain(int[][] pairs) {
        // sort by ascending second element
        Arrays.sort(pairs, (p1, p2) -> p1[1] - p2[1]);
        System.out.println(Arrays.deepToString(pairs));
        // iterate over sorted pairs list and compare second element to the next pair's first element
        int length = 0;
        long secondElem = Long.MIN_VALUE;
        for (int[] pair : pairs) {
            if (pair[0] > secondElem) {
                length += 1;
                secondElem = (long)pair[1];
            }
        }
        return length;
    }
}