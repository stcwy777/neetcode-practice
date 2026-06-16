class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dist = [[float('inf')] * N for _ in range(N)]
        heap = [(grid[0][0], 0, 0)]
        dist[0][0] = grid[0][0]

        while heap:
            elev, i, j = heapq.heappop(heap)
            
            if i == N - 1 and j == N - 1:
                return elev
            
            if elev > dist[i][j]:
                continue
            
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    new_elev = max(elev, grid[ni][nj])

                    if new_elev < dist[ni][nj]:
                        dist[ni][nj] = new_elev
                        heapq.heappush(heap, (new_elev, ni, nj))