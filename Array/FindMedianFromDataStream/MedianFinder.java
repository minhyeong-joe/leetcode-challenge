package Hard.FindMedianFromDataStream;

import java.util.ArrayList;
import java.util.List;

/**
 * Solution
 */
public class MedianFinder {

    private List<Integer> nums;

    /** initialize your data structure here. */
    public MedianFinder() {
        this.nums = new ArrayList<Integer>();
    }
    
    public void addNum(int num) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i) >= num) {
                nums.add(i, num);
                return;
            }
        }
        nums.add(num);
    }
    
    public double findMedian() {
        if (this.nums.size() == 0) {
            return -1;
        }
        if (this.nums.size() % 2 != 0) {
            // odd
            return this.nums.get((this.nums.size()-1)/2);
        } else {
            // even
            return (this.nums.get((this.nums.size()-1)/2) + this.nums.get(this.nums.size()/2)) / 2.0;
        }
    }
    
    public void print() {
        System.out.println(this.nums.toString());
    }
}