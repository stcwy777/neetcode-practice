class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        N = len(word)
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def explore(x: int, y: int, i: int) -> bool:
            
            if i == N:
                return True
            
            if x < 0 or y < 0 or x >= ROW or y >= COL:
                return False
            
            if board[x][y] != word[i]:
                return False

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                if explore(nx, ny, i + 1):
                    return True
                visited.remove((nx, ny))
        
        for i in range(ROW):
            for j in range(COL):
                visited.add((i, j))
                found = explore(i, j, 0)
                visited.remove((i, j))
                if found:
                    return True
        
        return False