'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. 
Otherwise, returns -1.

void put(int key, int value) Update the value of the key if present, or inserts 
the key if not already present. When the cache reaches its capacity, it should invalidate and 
remove the least frequently used key before inserting a new item. For this problem, when there is 
a tie (i.e., two or more keys with the same frequency), the least recently used key would be 
invalidated.

To determine the least frequently used key, a use counter is maintained for each key in 
the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the 
put operation). The use counter for a key in the cache is incremented either a get or 
put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
'''
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict() 
        ## usage[f][k]=v : frequency = f, key = k, v = value 
        self.usage = collections.defaultdict(collections.OrderedDict)
        ## current least frequenct usage
        self.LF = 0

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        ## update the frequency
        self.update(node, node.val)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key not in self.cache: 
            if len(self.cache) >= self.capacity:
                ## pop the node with current least freuenct usage (FIFO)
                k, v = self.usage[self.LF].popitem(last=False)
                self.cache.pop(k)
            node = ListNode(key, value)
            ## save the new node into cache and usage map
            self.cache[key] = node
            self.usage[1][key] = value
            ## reset current LF to 1
            self.LF = 1
        else: 
            ## update the vaLue of existing key 
            node = self.cache[key]
            node.val = value
            ## update the frequency
            self.update(node, value)
            
            
    def update(self, node, newVal):
        k, f = node.key, node.freq
        ## delete from the former frequency (f)
        self.usage[f].pop(k)
        ## if the former frequency is the LFU and it become empty
        ## the new frequency (f+1) become new LFU
        if not self.usage[f] and self.LF == f:
            self.LF += 1
        ## push to the new frequency (f+1)
        self.usage[f+1][k] = newVal
        node.freq += 1