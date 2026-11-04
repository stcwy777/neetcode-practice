from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stack.append(val)

    def pop(self) -> int:
        n = len(self.stack)
        max_freq = max(self.freq.values())
        val = 0

        for i in range(n - 1, -1, -1):
            val = self.stack[i]
            freq = self.freq[val]
            if freq == max_freq:
                self.freq[val] -= 1
                if i == n - 1:
                    self.stack = self.stack[:i]
                else:
                    self.stack = self.stack[:i] + self.stack[i + 1:]
                return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()