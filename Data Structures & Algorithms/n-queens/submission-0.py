class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        diag1 = set()
        diag2 = set()
        rslt = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                rslt.append([''.join(r) for r in board])
                return
            
            for i in range(n):
                if i in col or (row + i) in diag1 or (row - i) in diag2:
                    continue
                
                col.add(i)
                diag1.add(row + i)
                diag2.add(row - i)

                board[row][i] = 'Q'
                backtrack(row+1)
                board[row][i] = '.'
                
                col.remove(i)
                diag1.remove(row + i)
                diag2.remove(row - i)
        
        backtrack(0)

        return rslt

