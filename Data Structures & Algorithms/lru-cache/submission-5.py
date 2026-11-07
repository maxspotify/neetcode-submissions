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
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        node.prev = self.left
        node.next = self.left.next
        self.left.next.prev = node
        self.left.next = node

    def get(self, key: int) -> int:
        if key not in self.my_dict:
            return -1
        node = self.my_dict[key]
        self.delete(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            node = self.my_dict[key]
            node.val = value
            self.delete(node)
        else:
            node = Node(key, value)
            self.my_dict[key] = node

        self.insert(node)

        if len(self.my_dict) > self.capacity:
            lru = self.right.prev
            del self.my_dict[lru.key]
            self.delete(lru)
