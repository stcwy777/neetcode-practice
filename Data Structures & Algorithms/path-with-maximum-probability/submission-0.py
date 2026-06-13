class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = {}

        for i in range(n):
            adj[i] = []
        
        for i in range(len(edges)):
            a, b = edges[i]
            adj[a].append((succProb[i] * -1, b))
            adj[b].append((succProb[i] * -1, a))

        highest = {}

        minHeap = [(-1, start_node)]

        while minHeap:
            prob, node = heapq.heappop(minHeap)

            if node in highest:
                continue
            
            highest[node] = prob * -1

            for p, d in adj[node]:
                if d not in highest:
                    heapq.heappush(minHeap, (p * prob * -1, d))
        
        if end_node not in highest:
            return 0
        else:
            return highest[end_node]