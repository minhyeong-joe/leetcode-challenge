package Hard.MaximumScoreWords;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Solution
 */
public class Solution {

    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        int maxScore = 0;
        // create a map for word to its score
        Map<String, Integer> wordScoreMap = new HashMap<>();
        for (String word: words) {
            int wordScore = 0;
            for (char ch: word.toCharArray()) {
                wordScore += score[charToInt(ch)];
            }
            wordScoreMap.put(word, wordScore);
        }
        // count letters using array (due to lowercase letters constraint, no need to use memory-heavy map)
        int[] letterCount = new int[26];
        for (char letter: letters) {
            letterCount[charToInt(letter)]++;
        }
        // Create all subsets of words
        List<List<String>> allSubsets = new ArrayList<>();
        int numSubsets = (int) Math.pow(2, words.length);
        for (int i = 0; i < numSubsets; i++) {
            List<String> subset = new ArrayList<>();
            for (int j = 0; j < words.length; j++) {
                if ((i & (1 << j)) > 0) {
                    subset.add(words[j]);
                }
            }
            allSubsets.add(subset);
        }
        System.out.println(allSubsets.toString());
        // for each subset, check if all words in subset are "formable" and find max score
        boolean isFormable;
        for (List<String> ss: allSubsets) {
            int sum = 0;
            isFormable = true;
            int[] letterCountCopy = letterCount.clone();
            for (String word: ss) {
                // first check if word is "formable" using left-over letters
                for (char ch: word.toCharArray()) {
                    if (letterCountCopy[charToInt(ch)] <= 0) {
                        isFormable = false;
                        break;
                    }
                    letterCountCopy[charToInt(ch)]--;
                }
                // if word is formable, then add the score
                if (isFormable) {
                    sum += wordScoreMap.get(word);
                } else {
                    continue;
                }
            }
            System.out.println(ss.toString() + " : " + sum);
            if (sum > maxScore) {
                maxScore = sum;
            }
        }
        return maxScore;
    }

    // maps lowercase alphabet to ASCII integers with 'a' being base at 0 index
    private int charToInt(char c) {
        return (int)c - 97;
    }

}