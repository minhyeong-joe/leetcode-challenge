package Medium.CountSquareWithOnes;

import java.util.ArrayList;
import java.util.List;

/**
 * Solution
 */
public class Solution {

    public int countSquares(int[][] matrix) {
        int count = 0;
        // covert primitive int array into ArrayList for easier manipulation
        List<List<Integer>> mat = new ArrayList<>();
        for (int[] row: matrix) {
            List<Integer> list = new ArrayList<>();
            for (int num: row) {
                list.add(num);
            }
            mat.add(list);
        }
        // System.out.println("=== DEBUG: PRINT ARRAYLIST ===");
        // System.out.println(mat.toString());
        // go through each col by row
        for (int i = 0; i < mat.size(); i++) {
            for (int j = 0; j < mat.get(0).size(); j++) {
                // System.out.printf("=== %d, %d: %d ===\n", i, j, mat.get(i).get(j));
                if (i > 0 && j > 0 && mat.get(i).get(j) > 0) {
                    // accumulate
                    int min = Math.min(Math.min(mat.get(i-1).get(j), mat.get(i).get(j-1)), mat.get(i-1).get(j-1));
                    // System.out.println("MIN: " + min);
                    mat.get(i).set(j, mat.get(i).get(j)+min);
                }
                count += mat.get(i).get(j);
                // System.out.println("Count: " + count);
            }
        }
        return count;
    }
}