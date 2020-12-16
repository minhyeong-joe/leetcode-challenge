package Easy.IntersectionOfTwoArrays;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {

    // Test Driver
    public static void main(String[] args) {
        int[] nums1 = {1, 2, 2, 1}, nums2 = {2, 2};
        System.out.println("Input: nums1 = " + Arrays.toString(nums1) + " nums2 = " + Arrays.toString(nums2));
        int[] result = intersection(nums1, nums2);
        System.out.println("Output: " + Arrays.toString(result));

        System.out.println();

        int[] nums3 = {4, 9, 5}, nums4 = {9, 4, 9, 8, 4};
        System.out.println("Input: nums1 = " + Arrays.toString(nums3) + " nums2 = " + Arrays.toString(nums4));
        int[] result2 = intersection(nums3, nums4);
        System.out.println("Output: " + Arrays.toString(result2));
        
    }

    public static int[] intersection(int[] nums1, int[] nums2) {
        int[] result = new int[Math.max(nums1.length, nums2.length)];
        int i = 0;
        Map<Integer, Boolean> inNums1 = new HashMap<>();
        for (int v: nums1) {
            inNums1.put(v, true);
        }
        for (int v: nums2) {
            if (inNums1.containsKey(v)) {
                result[i++] = v;
                inNums1.remove(v);
            }
        }
        return Arrays.copyOfRange(result, 0, i);
    }

}