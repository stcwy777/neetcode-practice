class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        cost_heap = []
        profit_heap = []

        for i in range(len(capital)):
            heapq.heappush(cost_heap, (capital[i], i))

        # w
        while k > 0:
            # profit heap
            while cost_heap and cost_heap[0][0] <= w:
                c, i = heapq.heappop(cost_heap)
                heapq.heappush(profit_heap, (-profits[i], i))

            if not profit_heap:
                break

            p, i = heapq.heappop(profit_heap)
            w += -p
            k -= 1
        return w
