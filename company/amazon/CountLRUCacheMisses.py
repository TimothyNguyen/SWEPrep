from platform import node


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

def lruCacheMisses(num: int, pages: list, maxCacheSize: int) -> int:
    lookup = {}
    misses = 0
    size = 0
    HEAD = Node()
    TAIL = Node()

    for n in pages:
        if n in lookup:
            node = lookup[n]
            # ---- prev --> node --> next
            node.prev.next = node.next
            node.next.prev = node.prev

            HEAD.next.prev = node

            node.next = HEAD.next
            node.prev = HEAD

            HEAD.next = node

        else:
            # This value isn't in the cache yet
            misses += 1
            size += 1
             

            node = Node(n)
            lookup[n] = node

            # HEAD --> <-- 5
            # HEAD --><-- 3 --><-- 5 --><-- TAIL
            HEAD.next.prev = node
            node.next = HEAD.next
            HEAD.next = node
            if size > maxCacheSize:
                del lookup[TAIL.prev.value]
                TAIL.prev = TAIL.prev.prev
                TAIL.prev.prev.next = TAIL
                size -= 1
    return misses