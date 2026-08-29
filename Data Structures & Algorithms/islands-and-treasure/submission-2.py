from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()
        
        # 1. 找到所有的“宝箱/门”(0)，将它们作为多源 BFS 的起点全部入队
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. 从所有宝箱同时向外扩散 (BFS)
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in steps:
                nr, nc = r + dr, c + dc
                
                # 如果越界，或者不是空房间 (INF)，则跳过
                # 注意：这里隐式包含了对 -1 (墙) 和已访问过房间的过滤
                if not (0 <= nr < ROW and 0 <= nc < COL) or grid[nr][nc] != INF:
                    continue
                    
                # 记录距离，并把这个房间作为下一轮扩散的起点入队
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))