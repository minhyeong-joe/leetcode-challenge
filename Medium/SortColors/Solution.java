package Medium.SortColors;

import java.util.Arrays;

/**
 * Use 'low' to keep track of entry of next '0',
 * use 'middle' to iterate over color array
 * use 'high' to keep track of entry of next '2'
 */
public class Solution {

    public void sortColors(int[] nums) {
        int l = 0,
            m = 0,
            h = nums.length-1;
        while (m <= h) {
            switch (nums[m]) {
                case 0:
                    swap(nums, l, m);
                    l++;
                    // no break equivalent to
                    // m++; break; (because it flows to case 1)
                case 1:
                    m++;
                    break;
                case 2:
                    swap(nums, m, h);
                    h--;
                    break;
            }
        }
    }

    // helper swap function
    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    // test driver
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {2,0,2,1,1,0};
        System.out.println("Input: " + Arrays.toString(nums));
        sol.sortColors(nums);
        System.out.println("Output: " + Arrays.toString(nums));
    }

}