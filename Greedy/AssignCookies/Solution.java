package Easy.AssignCookies;

import java.util.Arrays;

/**
 * Solution
 */
public class Solution {

    // test driver
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] greeds = { 1, 2, 2, 1, 3, 5 };
        int[] sizes = { 1, 2, 2, 2, 2 };
        System.out.println(sol.findContentChildren(greeds, sizes));
    }

    public int findContentChildren(int[] g, int[] s) {
        int fed = 0;
        // sort both greed factors and cookie sizes
        Arrays.sort(g);
        Arrays.sort(s);
        System.out.println(Arrays.toString(g));
        System.out.println(Arrays.toString(s));
        int i = 0;
        int j = 0;
        while (i < g.length && j < s.length) {
            if (g[i] <= s[j]) {
                // feed the cookie
                fed++;
                i++;
            }
            j++;
        }
        return fed;
    }

}