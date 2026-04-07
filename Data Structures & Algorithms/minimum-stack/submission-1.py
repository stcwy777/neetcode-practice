class MinStack:

    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, val: int) -> None:
        # maintain a list of minimum value for every push
        if len(self._min) == 0 or self._min[-1] > val:
            self._min.append(val)
        else:
            self._min.append(self._min[-1])
        
        self._stack.append(val)

    def pop(self) -> None:
        self._stack = self._stack[:-1]
        self._min = self._min[:-1]

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min[-1]
