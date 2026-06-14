class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        # dist: 到每个点的最小“最大值”
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]

        # (cost, x, y)
        pq = [(grid[0][0], 0, 0)]

        while pq:
            cost, x, y = heapq.heappop(pq)

            if x == n - 1 and y == n - 1:
                return cost

            if cost > dist[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = max(cost, grid[nx][ny])

                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))

