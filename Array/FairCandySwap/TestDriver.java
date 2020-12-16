package Easy.FairCandySwap;

import java.util.Arrays;

public class TestDriver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] A1 = {1, 1},
              B1 = {2, 2};
        System.out.println("Input: A = " + Arrays.toString(A1) + ", B = " + Arrays.toString(B1));
        System.out.println("Output: " + Arrays.toString(sol.fairCandySwap(A1, B1)));

        int[] A2 = {1, 2},
              B2 = {2, 3};
        System.out.println("Input: A = " + Arrays.toString(A2) + ", B = " + Arrays.toString(B2));
        System.out.println("Output: " + Arrays.toString(sol.fairCandySwap(A2, B2)));

        int[] A3 = {2},
              B3 = {1, 3};
        System.out.println("Input: A = " + Arrays.toString(A3) + ", B = " + Arrays.toString(B3));
        System.out.println("Output: " + Arrays.toString(sol.fairCandySwap(A3, B3)));

        int[] A4 = {1, 2, 5},
              B4 = {2, 4};
        System.out.println("Input: A = " + Arrays.toString(A4) + ", B = " + Arrays.toString(B4));
        System.out.println("Output: " + Arrays.toString(sol.fairCandySwap(A4, B4)));
    }
}