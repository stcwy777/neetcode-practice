class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW, COL = len(board), len(board[0])

        checker = [(set(), set(), set()) for _ in range(9)]

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == '.':
                    continue

                digit = int(board[i][j]) 
                if 1 <= digit <= 9:
                    if i in checker[digit - 1][0] or j in checker[digit - 1][1] or (i//3 * 3 + j//3) in checker[digit - 1][2]:
                        return False
                    else:
                        checker[digit - 1][0].add(i)
                        checker[digit - 1][1].add(j)
                        checker[digit - 1][2].add((i//3 * 3 + j//3))
        
        return True
