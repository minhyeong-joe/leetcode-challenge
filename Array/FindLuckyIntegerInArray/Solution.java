package Easy.FindLuckyIntegerInArray;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    // Array with size 500 method
    // Leetcode submission: 1ms (faster than 99.45%), 39.2MB (less than 65.26%)
    public int findLucky(int[] arr) {
        // Using HashMap as frequency counter is good
        // but we can simply use array of size int[max] to reduce memory usage
        int[] frequency = new int[500];
        for (int num: arr) {
            frequency[num-1]++;
        }
        // System.out.println(Arrays.toString(frequency));
        // find the largest lucky number
        for (int i = frequency.length-1; i >= 0; i--) {
            if (i+1 == frequency[i]) {
                return i+1;
            }
        }
        return -1;
    }

    // HashMap method
    // Leetcode submission: 4ms (faster than 44.68%), 39.5MB (less than 42.53%)
    // public int findLucky(int[] arr) {
    //     Map<Integer, Integer> frequency = new HashMap<>();
    //     for (int num: arr) {
    //         if (frequency.containsKey(num)) {
    //             frequency.put(num, frequency.get(num)+1);
    //         } else {
    //             frequency.put(num, 1);
    //         }
    //     }
    //     // System.out.println(frequency.toString());
    //     List<Integer> luckyNumbers = new ArrayList<>();
    //     frequency.forEach((k,v) -> {
    //         if (k == v) {
    //             luckyNumbers.add(k);
    //         }
    //     });
    //     try {
    //         // System.out.println(Collections.max(luckyNumbers));
    //         return Collections.max(luckyNumbers);
    //     } catch (Exception e) {
    //         return -1;
    //     }
    // }
}