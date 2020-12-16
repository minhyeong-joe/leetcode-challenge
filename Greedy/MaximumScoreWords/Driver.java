package Hard.MaximumScoreWords;

public class Driver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] words = {"dog", "cat", "dad", "good"};
        char[] letters = {'a', 'a', 'c', 'd', 'd', 'd', 'g', 'o', 'o'};
        int[] scores = {1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0};
        System.out.println("Output: " + sol.maxScoreWords(words, letters, scores));
    }

}