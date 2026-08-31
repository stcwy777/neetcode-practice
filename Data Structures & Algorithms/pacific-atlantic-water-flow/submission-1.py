from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        ROW, COL = len(heights), len(heights[0])
        pac = set()
        atl = set()
        
        # 反向流动的 DFS，找寻“能够漫上去”的点
        def dfs(r, c, visit, prev_height):
            # 如果越界，或者已经访问过，或者当前高度比上一个格子低（水漫不上去），则停止
            if (r < 0 or c < 0 or r >= ROW or c >= COL or 
                (r, c) in visit or heights[r][c] < prev_height):
                return
            
            # 记录当前点可以到达对应的海洋
            visit.add((r, c))
            
            # 向四个方向继续漫水
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # 1. 从第一行（太平洋）和最后一行（大西洋）出发漫水
        for c in range(COL):
            dfs(0, c, pac, heights[0][c])           # 第一行：太平洋
            dfs(ROW - 1, c, atl, heights[ROW - 1][c]) # 最后一行：大西洋

        # 2. 从第一列（太平洋）和最后一列（大西洋）出发漫水
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])           # 第一列：太平洋
            dfs(r, COL - 1, atl, heights[r][COL - 1]) # 最后一列：大西洋

        # 3. 取交集，转化为题目要求的列表格式返回
        return list(pac & atl)