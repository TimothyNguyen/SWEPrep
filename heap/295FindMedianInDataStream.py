'''
The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of 
the actual answer will be accepted.

addNum()/findMedian():
- Time: O(log n)
Space: O(n)
'''
class MedianFinder:

    def __init__(self):
        self.minheap = [] 
        self.maxheap = [] 

    def addNum(self, num: int) -> None:
        # Maxheap will be at most one bigger than minheap
        heapq.heappush(self.maxheap, -num)
        
        # Convert to positive
        maxHeapTop = -heapq.heappop(self.maxheap)
        
        heapq.heappush(self.minheap, maxHeapTop)
        
        # Then balance
        if len(self.minheap) > len(self.maxheap):
            minHeapTop = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -minHeapTop)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return -self.maxheap[0]
        