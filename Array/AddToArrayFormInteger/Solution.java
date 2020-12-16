package Easy.AddToArrayFormInteger;

import java.util.ArrayList;
import java.util.List;

public class Solution {

    public List<Integer> addToArrayForm(int[] A, int K) {
        // convert int[] into List<Integer> to deal with addition overflow (increase in size)
        List<Integer> result = new ArrayList<>(A.length);
        for (int digit: A) {
            result.add(digit);
        }
        // System.out.println(result.toString());

        // start from right-end add corresponding digit from K
        for (int i = result.size()-1; i >=0; i--) {
            int sum = result.get(i) + (K%10);
            K /= 10;
            // if sum overflows (>= 10), then add abudant to K, and only take the one's digit as final sum
            if (sum >= 10) {
                K += sum/10;
                sum %= 10;
            }
            // System.out.println(sum);
            result.set(i, sum);
        }
        // deal with the remaining K
        while (K > 0) {
            result.add(0, K%10);
            K /= 10;
        }
        return result;
    }
    
}