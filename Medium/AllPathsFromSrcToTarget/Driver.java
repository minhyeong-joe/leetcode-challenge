package Medium.AllPathsFromSrcToTarget;

import java.util.Arrays;

public class Driver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] input = {{1,2},{3},{3},{}};
        System.out.println("Input: " + Arrays.deepToString(input));
        System.out.println("Output: " + sol.allPathsSourceTarget(input).toString());    
    }

}