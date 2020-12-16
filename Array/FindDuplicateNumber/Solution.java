package Medium.FindDuplicateNumber;

// Use Floyd's Tortoise and Hare Algorithm to detect cycle's entry point
// https://leetcode.com/problems/find-the-duplicate-number/solution/
// See approach 3 for detailed explanation.
// Key ideas
// Two phases:
// Phase 1: Hare runs double speed as tortoise, and where they meet is intersection in the cycle.
// Phase 2: Tortoise start from beginning, hare runs at tortoise's pace, where they meet again is the cycle's entry point.

class Solution {
    public int findDuplicate(int[] nums) {
        int slow = nums[nums[0]],
            fast = nums[slow];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        // move slower traversal back to starting
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}