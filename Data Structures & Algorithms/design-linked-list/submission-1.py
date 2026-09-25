class MyLinkedList:

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        node = self.get_node(index)
        if not node:
            return -1
        return node.val
    
    def get_node(self, index):
        if not self.head:
            return None

        node = self.head
        while index >= 0 and node:
            if index == 0:
                return node
            index -= 1
            node = node.next
        return None

    def addAtHead(self, val: int) -> None:
        head = self.ListNode(val, next=self.head)
        self.head = head

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = self.ListNode(val)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = self.ListNode(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        prev = self.get_node(index-1)
        nxt = prev.next
        if not prev:
            return
        prev.next = self.ListNode(val, nxt)
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return
        
        prev = self.get_node(index-1)
        if not prev.next:
            return
        
        prev.next = prev.next.next