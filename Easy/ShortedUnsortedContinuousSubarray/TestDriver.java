import java.util.Arrays;

class TestDriver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] input = { 2, 6, 4, 8, 10, 9, 15 };
        System.out.println("Input: " + Arrays.toString(input));
        System.out.println("Output: " + sol.findUnsortedSubarray(input));
        System.out.println();
    }
}