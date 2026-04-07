class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROW-1][COL-1] == 1:
            return -1
        
        visited = set()
        q = deque([(0, 0)])
        length = 1

        dir_eight = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == (ROW - 1) and c == (COL - 1):
                    return length
                for dir in dir_eight:
                    dr = r + dir[0]
                    dc = c + dir[1]
                    if dr >= ROW or dc >= COL or min(dr, dc) < 0 or grid[dr][dc] == 1  or (dr, dc) in visited:
                        continue                    
                    q.append((dr, dc))
                    visited.add((dr, dc))                    

            length += 1
        return -1