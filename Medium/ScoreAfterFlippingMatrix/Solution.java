package Medium.ScoreAfterFlippingMatrix;

import java.util.Arrays;

public class Solution {
    public int matrixScore(int[][] A) {
        int rowLength = A.length;
        int colLength = A[0].length;
        int sum = 0;
        // 1. flip to higher value per row (highest value is binary that begins with
        // '1')
        for (int[] row : A) {
            if (row[0] == 0) {
                flipRow(row);
            }
        }
        System.out.println("After row flipping: " + Arrays.deepToString(A));
        // 2. check by columns, flip to max the number of 1's
        // basically, if there are more zeros in the column, flip to make more 1's, if
        // equal number of zeros and ones, then no effect at all (as bit-wise, it's like
        // subtract 4 and add 4)
        for (int j = 0; j < colLength; j++) {
            int numZero = 0;
            for (int[] row : A) {
                if (row[j] == 0)
                    numZero++;
            }
            if (numZero > rowLength / 2) {
                flipCol(A, j);
            }
        }
        System.out.println("After col flipping: " + Arrays.deepToString(A));
        // 3. Lastly convert final array into binary and return sum
        for (int[] row : A) {
            sum += binaryArray(row);
        }
        return sum;
    }

    // helper function to flip row
    private void flipRow(int[] row) {
        for (int i = 0; i < row.length; i++) {
            row[i] = row[i] == 0 ? 1 : 0;
        }
    }

    // helper function to flip col
    private void flipCol(int[][] A, int colIndex) {
        for (int[] row : A) {
            row[colIndex] = row[colIndex] == 0 ? 1 : 0;
        }
    }

    // helper function to convert 1-d array to binary then to a decimal number
    private int binaryArray(int[] arr) {
        int decimal = 0;
        int power = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            decimal += arr[i] * Math.pow(2, power);
            power++;
        }
        return decimal;
    }
}