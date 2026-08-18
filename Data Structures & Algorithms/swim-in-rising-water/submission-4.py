class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        heap = [(grid[0][0], (0, 0))]
        dist = {}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            cost, (x, y) = heapq.heappop(heap)

            if (x, y) in dist:
                continue
            
            dist[(x, y)] = cost
            if x == n - 1 and y == n - 1:
                print(dist)
                return cost
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if nx >= n or ny >= n or nx < 0 or ny < 0:
                    continue

                heapq.heappush(heap, (max(cost, grid[nx][ny]), (nx, ny)))
        
        return dist[(n - 1, n - 1)]