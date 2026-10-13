from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        res = []
        n = len(tickets)

        for from_i, to_i in tickets:
            heapq.heappush(graph[from_i], to_i)
        
        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            res.append(node)
        dfs('JFK')
        return res[::-1]