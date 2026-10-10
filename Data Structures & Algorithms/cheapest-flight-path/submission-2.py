class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        stop = 0
        costs = [float('INF')] * n
        costs[src] = 0
        
        graph = [[] for _ in range(n)]
        for fi, ti, pi in flights:
            graph[fi].append((ti, pi))

        nodes = deque([(src, 0)])
        while nodes and stop <= k:
            
            for i in range(len(nodes)):
                node, base = nodes.popleft()
                for nbr, cost in graph[node]:
                    new_cost = cost + base
                    if new_cost < costs[nbr]:
                        costs[nbr] = new_cost
                        nodes.append((nbr, new_cost))
            stop += 1

        return -1 if costs[dst] == float('INF') else costs[dst]
                