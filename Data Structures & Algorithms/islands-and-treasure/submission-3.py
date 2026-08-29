from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in steps:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < ROW and 0 <= nc < COL) or grid[nr][nc] != INF:
                    continue
                    
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))