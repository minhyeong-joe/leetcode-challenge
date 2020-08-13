package Medium.MinStepsToMakeTwoStringsAnagram;

public class TestDriver {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "bab";
        String t = "aba";
        System.out.println("Input: s = " + s + ", t = " + t);
        System.out.println("Output: " + sol.minSteps(s, t));
        System.out.println();

        String s2 = "leetcode";
        String t2 = "practice";
        System.out.println("Input: s = " + s2 + ", t = " + t2);
        System.out.println("Output: " + sol.minSteps(s2, t2));
        System.out.println();

        String s3 = "friend";
        String t3 = "family";
        System.out.println("Input: s = " + s3 + ", t = " + t3);
        System.out.println("Output: " + sol.minSteps(s3, t3));
        System.out.println();
    }
}