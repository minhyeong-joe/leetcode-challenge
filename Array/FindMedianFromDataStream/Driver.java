package Hard.FindMedianFromDataStream;

public class Driver {
    
    public static void main(String[] args) {
        //  Your MedianFinder object will be instantiated and called as such:
        MedianFinder mf = new MedianFinder();
        mf.addNum(1);
        mf.addNum(2);
        mf.print();
        System.out.println("Output: " + mf.findMedian());
        mf.addNum(3);
        mf.print();
        System.out.println("Output: " + mf.findMedian());
        mf.addNum(6);
        mf.addNum(9);
        mf.print();
        System.out.println("Output: " + mf.findMedian());
        mf.addNum(5);
        mf.print();
        System.out.println("Output: " + mf.findMedian());
        mf.addNum(4);
        mf.print();
        System.out.println("Output: " + mf.findMedian());

    }

}