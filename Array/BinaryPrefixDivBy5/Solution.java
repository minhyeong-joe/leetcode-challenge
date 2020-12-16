package Easy.BinaryPrefixDivBy5;

import java.util.ArrayList;
import java.util.List;

/**
 * Solution
 */
public class Solution {

    public List<Boolean> prefixesDivBy5(int[] A) {
        List<Boolean> answer = new ArrayList<>();
        int sum = 0;
        for (int num: A) {
            sum += num;
            sum %= 5;
            answer.add(sum == 0);
            sum <<= 1;
        }
        return answer;
    }

}