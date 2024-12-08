class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.head = Node() # dummy
        self.tail = Node() # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def add_node(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        return node

    def remove_tail(self) -> Node:
        node = self.tail.prev
        self.remove_node(node)
        return node

    def move_node_to_front(self, node: Node):
        self.remove_node(node)
        self.add_node(node)

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self.move_node_to_front(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.value = value
            self.move_node_to_front(node)
            return
        new_node = Node()
        new_node.key = key
        new_node.value = value

        if self.curr_size == self.capacity:
            tail = self.remove_tail()
            self.curr_size -= 1
            del self.cache[tail.key]

        self.cache[key] = new_node
        self.add_node(new_node)
        self.curr_size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)