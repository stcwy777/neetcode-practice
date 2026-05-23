class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        if self.small and self.large and (self.small[0] * -1) > self.large[0]:
            heapq.heappush(self.large, self.small[0] * -1)
            heapq.heappop(self.small)

        if len(self.small) - 1 > len(self.large):
            heapq.heappush(self.large, self.small[0] * -1)            
            heapq.heappop(self.small)
        
        if len(self.large) - 1 > len(self.small):
            heapq.heappush(self.small, self.large[0] * -1)            
            heapq.heappop(self.large)


    def findMedian(self) -> float:

        if len(self.small) == len(self.large):
            return float(self.small[0] * -1 + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return self.small[0] * -1
        else:
            return self.large[0]

        
        