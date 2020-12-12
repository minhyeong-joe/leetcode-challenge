package Easy.PascalsTriangle;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascals = new ArrayList<>();
        // generate 0 to numRows-1 row
        for (int i = 0; i < numRows; i++) {
            List<Integer> pascal = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    pascal.add(1);
                } else {
                    pascal.add(pascals.get(i - 1).get(j - 1) + pascals.get(i - 1).get(j));
                }
            }
            pascals.add(pascal);
        }
        return pascals;
    }
}