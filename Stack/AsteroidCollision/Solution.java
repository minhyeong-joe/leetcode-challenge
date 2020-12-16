package Medium.AsteroidCollision;

import java.util.Stack;

/**
 * It's similar to checking balanced parentheses
 * Use stack
 */
public class Solution {

    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        // for each asteroid in order, if positive, then no effect on left-side so simply push to stack
        // if negative and has positive(s) previously, then check size and destroy the smaller one
        // if negative and has no positives in stack, then simply push to stack
        for (int asteroid: asteroids) {
            boolean destroyed = false;
            while (asteroid < 0 && !stack.empty() && stack.peek() > 0) {
                if (Math.abs(asteroid) > stack.peek()) {
                    stack.pop();
                } else if (Math.abs(asteroid) < stack.peek()) {
                    destroyed = true;
                    break;
                } else {
                    destroyed = true;
                    stack.pop();
                    break;
                }
            }
            if (!destroyed) {
                stack.push(asteroid);
            }
        }
        
        // convert to return type int[]
        int[] ans = new int[stack.size()];
        for (int i = 0; i < stack.size(); i++) {
            ans[i] = stack.get(i);
        }
        return ans;
    }

}