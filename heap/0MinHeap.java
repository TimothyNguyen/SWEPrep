import java.util.ArrayList;

public class MinHeap {
    
    // No capacity (arraylist)
    private int capacity;
    private int size = 0;
    ArrayList<Integer> items = new ArrayList<>();

    private int leftChildIndex(int parentIndex) { return 2 * parentIndex + 1; }
    private int rightChildIndex(int parentIndex) { return 2 * parentIndex + 2; }
    private int parentIndex(int childIndex) { return (childIndex - 1) / 2; }

    private boolean hasLeftChild(int index) { return leftChildIndex(index) < size; }
    private boolean hasRightChild(int index) { return rightChildIndex(index) < size; }
    private boolean hasParent(int index) { return parentIndex(index) >= 0; }

    private int leftChild(int index) { return items.get(leftChildIndex(index)); }
    private int rightChild(int index) { return items.get(rightChildIndex(index)); }
    private int parent(int index) { return items.get(parentIndex(index)); }

    private void swap(int i, int j) {
        int temp = items.get(i);
        items.set(i, items.get(j));
        items.set(j, temp);
    }

    public int peek() {
        if(size == 0) throw new IllegalStateException();
        return items.get(0); 
    }

    public int poll() {
        if(size == 0) throw new IllegalStateException();
        int item = items.get(0);
        items.set(0, items.get(size - 1));
        size--;
        heapifyDown();
        return item;
    }

    public void heapifyUp() {
        int index = size - 1;
        while(hasParent(index) && parent(index) > items.get(index)) {
            swap(parentIndex(index), index);
            index = parentIndex(index);
        }
    }

    public void heapifyDown() {
        int index = 0;
        while(hasLeftChild(index)) {
            int smallerChildIndex = leftChildIndex(index);
            if(hasRightChild(index) && rightChild(index) < leftChild(index))  smallerChildIndex = rightChildIndex(index);
            if(items.get(index) < items.get(smallerChildIndex)) break;
            else swap(index, smallerChildIndex);
            index = smallerChildIndex;
        }
    }


}
