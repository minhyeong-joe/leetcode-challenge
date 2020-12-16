package Easy.SqrtX;

/**
 * Solution
 */
public class Solution {

    public int mySqrt(int x) {
        if (x == 1) {
            return x;
        }
        long lower = 0;
        long upper = x;
        long check;
        // keep narrowing down, until upper and lower converge close enough for int result
        while (upper - lower > 1) {
            check = (lower+upper)/2;
            if (check*check > x) {
                upper = check;
            } else if (check*check < x) {
                lower = check;
            } else {
                return (int)check;
            }
        }

        return (int)lower;
    }
    
}