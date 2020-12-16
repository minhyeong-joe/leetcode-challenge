package Easy.ShortedUnsortedContinuousSubarray;

import java.util.Arrays;

// Sort array and check the length of unmatching subarray

class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int[] sorted = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sorted);
        // System.out.println(Arrays.toString(sorted));
        // System.out.println(Arrays.toString(nums));
        int start = 0;
        int end = 0;
        // first difference is the start index of contiguous subarray
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != sorted[i]) {
                start = i;
                break;
            }
        }
        // first difference from backwards is the end index of contiguous subarray
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] != sorted[i]) {
                end = i;
                break;
            }
        }
        // System.out.println(start);
        // System.out.println(end);

        return start != end ? end - start + 1 : 0;
    }
}