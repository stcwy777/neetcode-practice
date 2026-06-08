class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n + 1):
            adj[i] = []

        for u, v, t in times:
            adj[u].append((v, t))
        
        shortest = {}
        minHeap = [(0, k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in shortest:
                continue
            shortest[node] = time

            for des, extraT in adj[node]:
                if des not in shortest:
                    heapq.heappush(minHeap, (time + extraT, des))
        if len(shortest) < n:
            return -1
        else:
            return max(shortest.values())
        