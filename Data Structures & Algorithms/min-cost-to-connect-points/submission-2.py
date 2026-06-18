class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {}
        for i in range(N):
            adj[i] = []
        for i in range(N):
            for j in range(i + 1, N):
                manDis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                adj[i].append((manDis, j))
                adj[j].append((manDis, i))
        
        visit = set()
        edges = []
        heap = [(0, 0)]
        while heap:
            if len(visit) == N or len(edges) == N - 1:
                break
            dis, des = heapq.heappop(heap)

            if des in visit:
                continue
            visit.add(des)
            if dis:
                edges.append(dis)
            for nDis, nDes in adj[des]:
                if nDes in visit:
                    continue
                heapq.heappush(heap, (nDis, nDes))

        return sum(edges)