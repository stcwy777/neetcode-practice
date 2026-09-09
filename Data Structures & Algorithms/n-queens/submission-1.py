class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]

        col = set()
        diag1 = set()
        diag2 = set()
        res = []

        def dfs(r: int) -> None:
            if r == n:
                res.append([''.join(x) for x in board])
                return
            
            for c in range(n):
                if c in col or (r + c) in diag1 or (r - c) in diag2:
                    continue
                else:
                    col.add(c)
                    diag1.add(r + c)
                    diag2.add(r - c)
                    board[r][c] = 'Q'
                    dfs(r + 1)
                    col.remove(c)
                    diag1.remove(r + c)
                    diag2.remove(r - c)
                    board[r][c] = '.'                        
            return
        
        dfs(0)
        return res