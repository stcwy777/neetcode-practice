class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        q = deque()
        visited = set()
        fruits = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                    fruits += 1
                elif grid[i][j] == 1:
                    fruits += 1
        
        adjacents = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rottens = 0
        mins = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rottens += 1

                for adj in adjacents:
                    dr = r + adj[0]
                    dc = c + adj[1]

                    if dr >= ROW or dc >= COL or min(dr, dc) < 0 or (dr, dc) in visited or grid[dr][dc] == 0:
                        continue
                    
                    q.append((dr, dc))
                    visited.add((dr, dc))
        
            mins += 1
        if rottens == fruits:
            if fruits == 0:
                return 0
            else:
                return mins
        else:
            return -1
                