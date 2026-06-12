class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n + 1):
            adj[i] = []

        for ui, vi, ti in times:
            adj[ui].append((vi, ti))

        shortest = {}
        heap = [(0, k)]
        
        while heap:
            time, dst = heapq.heappop(heap)

            if dst in shortest:
                continue           
            shortest[dst] = time
            
            for node, t in adj[dst]:
                if node not in shortest:
                    heapq.heappush(heap, (time + t, node))

        if len(shortest) < n:
            return -1
        else:
            return max(shortest.values())
        
        