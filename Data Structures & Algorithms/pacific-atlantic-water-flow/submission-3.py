class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r: int, c:int, visited: Set[(int, int)], prevHeight: int) -> None:

            if not (0 <= r < ROW and 0 <= c < COL) or (r, c) in visited or heights[r][c] < prevHeight:
                return
            
            visited.add((r, c))

            for (x, y) in steps:
                nr = r + x
                nc = c + y

                dfs(nr, nc, visited, heights[r][c])
            
            return
        
        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COL - 1, atlantic, heights[r][COL - 1])

        for c in range(COL):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROW - 1, c, atlantic, heights[ROW - 1][c])

        return list(pacific & atlantic)