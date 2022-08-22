'''
Design a data structure that follows the constraints of a 
Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise 
return -1.

void put(int key, int value) Update the value of the key if the key exists. 

Otherwise, add the key-value pair to the cache. If the number of keys 
exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity. 

IDEA:
Have a cache
head and tail nodes are dummy nodes
'''
class Node():
    def __init__(self) -> None:
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

class LRUCache():
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)
    
    def remove_tail(self):
        node = self.tail.prev
        self.remove(node)
        return node

    def __init__(self, capacity) -> None:
        self.head = Node()
        self.tail = Node()
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        node = self.cache.get(key)
        if node:
            self.move_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        node = self.cache.get(key)
        if node:
            node.value = value
            self.move_to_head(node)
            return
        
        node = Node()
        node.key = key
        node.value = value
        self.move_to_head(node)
        self.cache[key] = node
        if self.size == self.capacity:
            tail = self.remove_tail()
            del self.cache[tail.key]
        else:
            self.size += 1

        