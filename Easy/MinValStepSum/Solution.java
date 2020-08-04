// Let positive start value be X
// For each num in nums:
//     the step sum value is X + num[0], X + num[0] + num[1]...
// so for each num, the sum value is X + SUM(num so far)
// we just need to guarantee that sum value is positive for any SUM(num so far)

package Easy.MinValStepSum;

/**
 * Solution
 */
public class Solution {

    public int minStartValue(int[] nums) {
        int startVal = 1;
        int sum = 0;
        for (int num : nums) {
            sum += num;
            if (startVal + sum < 1) {
                startVal = 1 - sum;
            }
        }
        return startVal;
    }

}