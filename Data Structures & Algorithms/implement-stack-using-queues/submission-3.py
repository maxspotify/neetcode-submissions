class MyStack:
# better sol 1: one queue, O(n) pop, O(1) top, push, one queue , o(1) space
    def __init__(self):
        self.queue = deque()
        self.my_top = None

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.my_top = x

    def pop(self) -> int:
        print(self.queue)
        len_queue = len(self.queue) # O(1)
        while len_queue > 1:
            popped_val = self.queue.popleft()
            if len_queue == 2:
                self.my_top = popped_val
            self.queue.append(popped_val)
            len_queue -= 1
        ret = self.queue.popleft()
        if self.empty():
            self.my_top = None
        return ret

    def top(self) -> int:
        return self.my_top

    def empty(self) -> bool:
        return not len(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()