package Easy.IsomorphicStrings;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * For each char in 's', add a corresponding char in 't' if not seen before,
 * else check if char in 't' maps to the correct char
 */
public class Solution {

    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> mapping = new HashMap<>();
        Set<Character> seen = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            // if char is 's' exists in mapping, return false if mapping does not match
            // actual char in 't'
            if (mapping.containsKey(s.charAt(i))) {
                if (mapping.get(s.charAt(i)) != t.charAt(i)) {
                    return false;
                }
            }
            // if mapping already exists for different key, return false (ie. ab->aa;
            // a:a, 'b' cannot map to 'a')
            else {
                if (seen.contains(t.charAt(i))) {
                    return false;
                }
            }
            // else add char in 's' and char in 't' to mapping
            mapping.putIfAbsent(s.charAt(i), t.charAt(i));
            seen.add(t.charAt(i));
            // System.out.println(mapping.toString());
            // System.out.println(seen.toString());
        }
        return true;
    }

}