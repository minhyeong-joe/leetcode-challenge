package Medium.UniquePaths;

class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 1 && n == 1) {
            return 1;
        }
        int[][] dpPaths = new int[m][n];
        // print out Dynamic Programming table for debugging
        // for (int row = 0; row < n; row++) {
        //     for (int col = 0; col < m; col++) {
        //         System.out.printf("%d ", dpPaths[col][row]);
        //     }
        //     System.out.println();
        // }
        // initialize constant paths
        // all bottom ones have only one path to right, all right ones have only one path to bottom
        for (int col = 0; col < m-1; col++) {
            dpPaths[col][n-1] = 1;
        }
        for (int row = 0; row < n-1; row++) {
            dpPaths[m-1][row] = 1;
        }
        // now bottom-up construct dp table all the way to start point
        for (int row = n-2; row >= 0; row--) {
            for (int col = m-2; col >=0; col--) {
                dpPaths[col][row] = dpPaths[col+1][row] + dpPaths[col][row+1];
            }
        }
        // print out Dynamic Programming table for debugging
        // for (int row = 0; row < n; row++) {
        //     for (int col = 0; col < m; col++) {
        //         System.out.printf("%d ", dpPaths[col][row]);
        //     }
        //     System.out.println();
        // }
        return dpPaths[0][0];
    }
}