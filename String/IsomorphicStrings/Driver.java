package Easy.IsomorphicStrings;

public class Driver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        String s1 = "egg";
        String t1 = "add";
        System.out.println("Input: s = " + s1 + ", t = " + t1);
        System.out.println("Output: " + sol.isIsomorphic(s1, t1)); 
        System.out.println();

        String s2 = "foo";
        String t2 = "bar";
        System.out.println("Input: s = " + s2 + ", t = " + t2);
        System.out.println("Output: " + sol.isIsomorphic(s2, t2)); 
        System.out.println();

        String s3 = "paper";
        String t3 = "title";
        System.out.println("Input: s = " + s3 + ", t = " + t3);
        System.out.println("Output: " + sol.isIsomorphic(s3, t3)); 
        System.out.println();
    }

}