package Medium.CountSquareWithOnes;

public class Driver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] matrix = {{0,1,1,1}, {1,1,1,1}, {0,1,1,1}};
        System.out.println("output: " + sol.countSquares(matrix));
    }

}
