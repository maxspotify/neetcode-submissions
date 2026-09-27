class MyStack:

    def __init__(self):
        self.queue = deque()
        self.helper = deque()

    def push(self, x: int) -> None:
        self.helper.append(x)
        while self.queue:
            self.helper.append(self.queue.popleft())
        
        self.queue = self.helper
        self.helper = deque()

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not len(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()