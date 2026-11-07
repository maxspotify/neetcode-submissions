class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.my_dict = {}
        self.capacity = capacity
        self.size = 0
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def delete(self, key):
        node = self.my_dict[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.my_dict[key]
        self.size -= 1
    
    def insert(self, key, value):
        node = Node(key, value)
        self.my_dict[key] = node
        node.prev = self.left
        node.next = self.left.next
        self.left.next.prev = node
        self.left.next = node
        self.size += 1

    def get(self, key: int) -> int:
        if key not in self.my_dict:
            return -1
        node = self.my_dict[key]
        self.delete(key)
        self.insert(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            self.delete(key)
    
        self.insert(key, value)

        if self.size > self.capacity:
            lru = self.right.prev
            self.delete(lru.key)
