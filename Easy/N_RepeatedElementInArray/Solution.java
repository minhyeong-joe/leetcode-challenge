package Easy.N_RepeatedElementInArray;

import java.util.HashSet;
import java.util.Set;

/**
 * Solution
 * "Size of 2N with N+1 unique Elements, and one element repeats N times" means that other elements will only appear once.
 * ie) N=5, Size=10, 6 unique elements => 1,2,3,4,5,6,6,6,6,6 (no more space for other duplicates)
 * So using haveSeen Set to find a duplicate is all that's needed
 */
public class Solution {

    public int repeatedNTimes(int[] A) {
        Set<Integer> seen = new HashSet<>();
        for (int num: A) {
            if (seen.contains(num)) {
                return num;
            }
            seen.add(num);
        }
        return -1;
    }

}