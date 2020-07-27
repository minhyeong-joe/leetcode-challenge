package Medium.UniquePaths;

public class Driver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int m1 = 3, n1 = 2;
        System.out.printf("Input: m = %d, n = %d\n", m1, n1);
        System.out.println("Output: " + sol.uniquePaths(m1, n1));

        System.out.println();
        
        int m2 = 7, n2 = 3;
        System.out.printf("Input: m = %d, n = %d\n", m2, n2);
        System.out.println("Output: " + sol.uniquePaths(m2, n2));

        System.out.println();

        int m3 = 23, n3 = 12;
        System.out.printf("Input: m = %d, n = %d\n", m3, n3);
        System.out.println("Output: " + sol.uniquePaths(m3, n3));
    }

}