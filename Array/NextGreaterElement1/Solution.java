package Easy.NextGreaterElement1;

import java.util.Arrays;

class Solution {

    public static void main(String[] args) {
        // int nums1[] = {4, 1, 2};
        // int nums2[] = {1, 3, 4, 2};

        int nums1[] = {2, 4};
        int nums2[] = {1, 2, 3, 4};
        
        int answer[] = nextGreaterElement(nums1, nums2);

        System.out.println(Arrays.toString(answer));
    }

    public static int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int answer[] = new int[nums1.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = -1;
        }
        for (int i = 0; i < nums1.length; i++) {
            for (int j = find(nums2, nums1[i]); j < nums2.length; j++) {
                if (nums2[j] > nums1[i]) {
                    answer[i] = nums2[j];
                    break;
                }
            }
        }
        return answer;
    }

    public static int find(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }
}