package Easy.ThirdMaximumNumber;

/**
 * Solution
 */
public class Solution {

    public int thirdMax(int[] nums) {
        long max = Long.MIN_VALUE;
        long secondMax = Long.MIN_VALUE;
        long thirdMax = Long.MIN_VALUE;
        for (int n : nums) {
            if (n > max) {
                thirdMax = secondMax;
                secondMax = max;
                max = (long)n;
            } else if (n > secondMax && n < max) {
                thirdMax = secondMax;
                secondMax = (long)n;
            } else if (n > thirdMax && n < secondMax) {
                thirdMax = (long)n;
            }
        }
        if (thirdMax == Long.MIN_VALUE)
            return (int)max;
        return (int)thirdMax;
    }
    
}