import heapq
class MedianFinder:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
    
    def addNum(self, num: int) -> None:
        # maxheap length is either equal or 1 greater than minheap length
        # always store negative value for maxheap
        heapq.heappush(self.maxheap, -num)
        
        # Convert to positive when retrieving from maxheap
        maxHeapTop = -heapq.heappop(self.maxheap)

        heapq.heappush(self.minheap, maxHeapTop)

        # Balance two heaps
        if len(self.minheap) > len(self.maxheap):
            minHeapTop = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -minHeapTop)
    
    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-self.maxheap[0])) / 2
        else:
            return -self.maxheap[0]