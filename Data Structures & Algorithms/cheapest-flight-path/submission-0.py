class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        dist = [float("inf")] * n
        dist[src] = 0

        q = deque([(src, 0)])

        stops = 0

        while q and stops <= k:

            size = len(q)

            temp = dist[:]

            for _ in range(size):

                city, cost = q.popleft()

                for nei, price in graph[city]:

                    if cost + price < temp[nei]:

                        temp[nei] = cost + price

                        q.append((nei, cost + price))

            dist = temp
            stops += 1

        return -1 if dist[dst] == float("inf") else dist[dst]