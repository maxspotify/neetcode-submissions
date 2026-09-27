class MyStack:
# bad solution
    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        result = deque()
        last_elem = len(self.queue) - 1
        ret = 0
        for i in range(len(self.queue)):
            if i != (last_elem):
                val = self.queue.popleft()
                result.append(val)
            else:
                ret = self.queue.popleft()
        self.queue = result
        return ret

        

    def top(self) -> int:
        result = deque()
        last_elem = (len(self.queue) - 1)
        for i in range(len(self.queue)):
            val = self.queue.popleft()
            result.append(val)
            if i == last_elem:
                self.queue = result
                return val
        

    def empty(self) -> bool:
        return not len(self.queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()