class MyQueue {

    private Stack<Integer> s1, s2;
    private int size;
    /** Initialize your data structure here. */
    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
        size = 0;
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        s1.push(x);
        size++;
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if(size == 0) throw new IllegalStateException();
        while(size > 1) {
            s2.push(s1.pop());
            size--;
        }
        int temp = s1.pop();
        size--;
        while(!s2.isEmpty()) {
            s1.push(s2.pop());
            size++;
        }
        return temp;
    }
    
    /** Get the front element. */
    public int peek() {
        if(size == 0) throw new IllegalStateException();
        while(size > 1) {
            s2.push(s1.pop());
            size--;
        }
        int temp = s1.peek();
        while(!s2.isEmpty()) {
            s1.push(s2.pop());
            size++;
        }
        return temp;
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return size == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */