package Easy.MaxProductofThreeNumbers;

import java.util.Arrays;

/**
 * Solution
 */
public class Solution {

    // First sort the array
    // Two possible cases involving negative elements:
    // 1. The product of two negatives > The product of third and second max positives
    // 2. The product of two negatives < The product of third and second max positives
    // (if equal, it does not matter which pair we choose)

    public int maximumProduct(int[] nums) {
        if (nums.length < 3) {
            return 0;
        }
        Arrays.sort(nums);
        int product = 1;
        if (nums[0] < 0 && nums[1] < 0 && nums[0]*nums[1] >= nums[nums.length-3]*nums[nums.length-2]) {
            product = nums[0]*nums[1]*nums[nums.length-1];
        } else {
            product = nums[nums.length-3]*nums[nums.length-2]*nums[nums.length-1];
        }
        return product;
    }

}