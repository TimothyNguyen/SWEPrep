class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

class LRUCache:

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
        self.remove_node(node)
        return node
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        
        # move to head
        self.move_to_head(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.value = value
            self.move_to_head(node)
            return
        
        node = Node()
        node.key = key
        node.value = value
        self.cache[key] = node
        self.add_node(node)

        if self.size < self.capacity:
            self.size += 1
        else:
            tail = self.remove_tail()
            del self.cache[tail.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)