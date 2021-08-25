class LRUCache:

    class Node:
        def __init__(self):
            self.key = 0
            self.value = 0
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.head = self.Node()
        self.tail = self.Node()
        self.capacity = capacity
        self.nodeMap = dict()

    def _add(self, node):
        headNext = self.head.next
        node.next = headNext
        headNext.prev = node
        self.head.next = node
        node.prev = self.head

    def _remove(self, node):
        nextNode = node.next
        prevNode = node.prev
        nextNode.prev = prevNode
        prevNode.next = nextNode

    def get(self, key: int) -> int:
        result = -1
        node = self.nodeMap.get(key)
        if node:
            result = node.val
            self.remove(node)
            self.add(node)
        return result

    def put(self, key: int, value: int) -> None:
        node = self.nodeMap.get(key)
        if node:
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            # Capacity check
            if len(self.nodeMap) == self.capacity:
                self.nodeMap.remove(self.tail.prev.key)
                self.remove(self.tail.prev)
            
            newNode = self.Node()
            newNode.key = key
            newNode.value = value

            self.nodeMap.put(key, newNode)
            self._add(newNode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)