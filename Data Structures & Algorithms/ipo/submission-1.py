class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cap_heap = []
        prof_heap = []
        
        for i in range(len(capital)):
            heapq.heappush(cap_heap, (capital[i], i))        
        
        while k:

            while cap_heap and cap_heap[0][0] <= w:
                cap, idx = heapq.heappop(cap_heap)
                heapq.heappush(prof_heap, (-1 * profits[idx], idx))
            
            if not prof_heap:
                break
            prof, idx = heapq.heappop(prof_heap)

            w += -1 * prof
            k -= 1
        
        return w


            



