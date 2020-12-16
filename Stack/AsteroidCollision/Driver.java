package Medium.AsteroidCollision;

import java.util.Arrays;

public class Driver {
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] asteroids = {5, 10, -5};
        System.out.println("Input: asteroids = " + Arrays.toString(asteroids));
        System.out.println("Output: " + Arrays.toString(sol.asteroidCollision(asteroids)));    
    }

}