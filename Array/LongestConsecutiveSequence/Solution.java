package Hard.LongestConsecutiveSequence;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Because of O(N) time complexity restriction,
 * use Set (as we don't need key:value) to make lookup O(1) 
 */
public class Solution {

    public int longestConsecutive(int[] nums) {
        // System.out.println(Arrays.toString(nums));
        int longest = 0;
        Set<Integer> numSet = new HashSet<>();
        // add array elements to set for O(1) lookup
        for (int num: nums) {
            numSet.add(num);
        }
        // System.out.println(numSet.toString());
        // iterate N elements and start counting sequence iff num is the first of consecutive
        for (int num: nums) {
            if (!numSet.contains(num-1)) {
                int currentNum = num;
                int consecutive = 1;
                while (numSet.contains(currentNum+1)) {
                    consecutive++;
                    currentNum++;
                }
                longest = consecutive > longest? consecutive: longest;
            }
        }
        return longest;
    }

}