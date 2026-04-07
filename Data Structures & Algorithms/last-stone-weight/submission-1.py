class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq.heapify_max(stones)
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)
            c = abs(a - b)
            print(a,b,c)
            if c > 0:
                heapq.heappush_max(stones, c)
                        
        if not len(stones):
            return 0
        elif len(stones) == 1:
            return stones[0]