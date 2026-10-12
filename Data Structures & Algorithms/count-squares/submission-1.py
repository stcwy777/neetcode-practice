from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.X = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        
        self.X[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]

        if x not in self.X:
            return 0
        
        count = 0
        for dy, freq in self.X[x].items():
            delta = y - dy 

            if delta == 0:
                continue

            count += freq * self.X[x + delta][y] * self.X[x + delta][dy]
            count += freq * self.X[x - delta][y] * self.X[x - delta][dy]

        return count