class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        
        n = len(matrix[0])
        if n == 0:
            return False
        
        lp = 0
        rp = m * n - 1

        while lp <= rp:
            mp = lp + (rp - lp) // 2

            mp_row = mp // n
            mp_col = mp - mp_row * n
            if matrix[mp_row][mp_col] == target:
                return True
            elif matrix[mp_row][mp_col] < target:
                lp = mp + 1
            else:
                rp = mp - 1
        return False

        