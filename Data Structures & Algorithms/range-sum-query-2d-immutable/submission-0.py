class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._row = len(matrix)
        self._col = len(matrix[0])
        self._pref_matrix = [[0] * (self._col + 1) for _ in range(self._row + 1)]

        for i in range(1, self._row + 1):
            for j in range(1, self._col + 1):
                self._pref_matrix[i][j] = matrix[i - 1][j - 1] + self._pref_matrix[i - 1][j] + self._pref_matrix[i][j - 1] - self._pref_matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        l_row, l_col = row1 + 1, col1 + 1
        r_row, r_col = row2 + 1, col2 + 1

        return self._pref_matrix[r_row][r_col] - self._pref_matrix[r_row][l_col - 1] - self._pref_matrix[l_row - 1][r_col] + self._pref_matrix[l_row - 1][l_col - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)