class LRUCache(object):
    class DListNode(object):
        def __init__(self, k, v):
            self.key = k
            self.val = v
            self.next = None
            self.prev = None


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash_table = {}
        self.head = LRUCache.DListNode(-1, -1)
        self.tail = LRUCache.DListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def put_node_to_tail(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_table:
            node = self.hash_table[key]
            self.put_node_to_tail(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash_table:
            node = self.hash_table[key]
            node.val = value
            self.put_node_to_tail(node)
        else:
            node = LRUCache.DListNode(key, value)
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            self.hash_table[key] = node
            if self.size < self.capacity:
                self.size += 1
            else:
                del_node = self.head.next
                self.head.next = del_node.next
                del_node.next.prev = self.head
                del self.hash_table[del_node.key]


if __name__ == "__main__":
    c = LRUCache(3)
    print c.put(1, 1)
    print c.put(2, 2)
    print c.put(3, 3)
    print c.put(4, 4)
    print c.get(4)
    print c.get(3)
    print c.get(2)
    print c.get(1)
    print c.put(5, 5)
    print c.get(1)
    print c.get(2)
    print c.get(3)
    print c.get(4)
    print c.get(5)