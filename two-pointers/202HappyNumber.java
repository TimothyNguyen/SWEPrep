class Solution {
    public boolean isHappy(int n) {
        int slow = n, fast = getNext(n);
        while(fast != slow && fast != 1) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        } 
        return fast == 1;
    }
    
    public int getNext(int n) {
        int squareSum = 0;
        while(n > 0) {
            squareSum += Math.pow(n % 10, 2);
            n /= 10;
        }
        return squareSum;
    }
}