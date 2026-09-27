class MyStack:
# bad solution
    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        result = deque()
        ret = 0
        for i in range(len(self.queue)):
            if i != (len(self.queue) - 1):
                result.append(self.queue[i])
            else:
                ret = self.queue[i]
        self.queue = result
        return ret

        

    def top(self) -> int:
        for i in range(len(self.queue)):
            if i == len(self.queue) - 1:
                return self.queue[i]
        

    def empty(self) -> bool:
        return not len(self.queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()