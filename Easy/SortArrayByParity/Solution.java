package Easy.SortArrayByParity;

/**
 * 
 */
public class Solution {

    public int[] sortArrayByParity(int[] A) {
        int evenIndex = -1;
        for (int i = 0; i < A.length; i++) {
            if (A[i] % 2 != 0) {
                // if odd
                // initialize first even index
                if (evenIndex < 0) {
                    evenIndex = i;
                }
                while (evenIndex < A.length-1 && A[evenIndex] % 2 != 0) {
                    evenIndex++;
                }
                swap(A, i, evenIndex);
            }
        }
        return A;
    }

    private void swap(int[] A, int i, int j) {
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
    
}