class MyStack:

    def __init__(self):
        self._queues = [[], []]
        self._active = 0 

    def push(self, x: int) -> None:
        self._queues[self._active].append(x)

    def pop(self) -> int:
        x = None
        for i in range(len(self._queues[self._active]) - 1):
            x = self._queues[self._active].pop(0)
            self._queues[(self._active + 1) % 2].append(x)

        x = self._queues[self._active].pop(0)
        self._active = (self._active + 1) % 2
        return x

    def top(self) -> int:
        x = None
        for i in range(len(self._queues[self._active])):
            x = self._queues[self._active].pop(0)
            self._queues[(self._active + 1) % 2].append(x)
        
        self._active = (self._active + 1) % 2
        return x        

    def empty(self) -> bool:
        if len(self._queues[self._active]) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()