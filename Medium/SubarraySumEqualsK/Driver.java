package Medium.SubarraySumEqualsK;

import java.util.Arrays;

public class Driver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1,1,1,2,1,2,3,5};
        int K = 5;
        System.out.println("Input: nums = " + Arrays.toString(nums) + ", k = " + K);
        System.out.println("Output: " + sol.subarraySum(nums, K));
    }
}