package Easy.MinValStepSum;

import java.util.Arrays;

public class TestDriver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int nums1[] = {-3, 2, -3, 4, 2};
        System.out.println("Input: nums = " + Arrays.toString(nums1));
        System.out.println("Output: " + sol.minStartValue(nums1));
        System.out.println();

        int nums2[] = {1, 2};
        System.out.println("Input: nums = " + Arrays.toString(nums2));
        System.out.println("Output: " + sol.minStartValue(nums2));
        System.out.println();

        int nums3[] = {1, -2, -3};
        System.out.println("Input: nums = " + Arrays.toString(nums3));
        System.out.println("Output: " + sol.minStartValue(nums3));
        System.out.println();
    }

}