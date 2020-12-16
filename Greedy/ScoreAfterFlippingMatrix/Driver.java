package Medium.ScoreAfterFlippingMatrix;

public class Driver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] input = { { 0, 0, 1, 1 }, { 1, 0, 1, 0 }, { 1, 1, 0, 0 } };
        System.out.println(sol.matrixScore(input));
    }
}
