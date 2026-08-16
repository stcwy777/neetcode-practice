class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker = {}

        for i in range(1, 10):
            checker[i] = { 'row': set(), 'col': set(), 'box': set()}

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    box =  (i // 3, j // 3)
                    if i in checker[val]['row'] or j in checker[val]['col'] or box in checker[val]['box']:
                        return False
                    else:
                        checker[val]['row'].add(i)
                        checker[val]['col'].add(j)
                        checker[val]['box'].add(box)
        
        return True