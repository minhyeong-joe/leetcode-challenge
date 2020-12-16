package Medium.MinStepsToMakeTwoStringsAnagram;

import java.util.HashMap;
import java.util.Map;

// Create a dictionary with all characters of both strings, with counter initialized as 0
// +1 for any characters in first string, -1 for any characters in second string
// at the end, the sum of positives is the min step (at this time, the sum of all counters should be 0, this can be used as validation)

class Solution {
    public int minSteps(String s, String t) {
        Map<Character, Integer> countMap = new HashMap<>();
        for (char c: s.toCharArray()) {
            if (countMap.containsKey(c)) {
                countMap.put(c, countMap.get(c)+1);
            } else {
                countMap.put(c, 1);
            }
        }
        for (char c: t.toCharArray()) {
            if (countMap.containsKey(c)) {
                countMap.put(c, countMap.get(c)-1);
            } else {
                countMap.put(c, -1);
            }
        }
        // System.out.println(countMap.toString());
        // check sum of negatives and positives
        int sumPos = 0;
        int sumNeg = 0;
        for (int v: countMap.values()) {
            if (v > 0) {
                sumPos += v;
            } else if (v < 0) {
                sumNeg += v;
            }
        }
        // validate
        return sumPos + sumNeg == 0? sumPos: -1;
    }
}