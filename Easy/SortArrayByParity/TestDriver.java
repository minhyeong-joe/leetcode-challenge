package Easy.SortArrayByParity;

import java.util.Arrays;

public class TestDriver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] A = {3, 1, 2, 4, 5};
        System.out.println("Output: " + Arrays.toString(sol.sortArrayByParity(A)));
    }

}