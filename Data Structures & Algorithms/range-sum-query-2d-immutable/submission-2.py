class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._row = len(matrix)
        self._col = len(matrix[0])

        self._preSum = [[0] * (self._col + 1) for _ in range(self._row + 1)]
        for i in range(1, self._row + 1):
            for j in range(1, self._col + 1):
                self._preSum[i][j] = self._preSum[i - 1][j] + self._preSum[i][j - 1] - self._preSum[i - 1][j - 1] + matrix[i - 1][j - 1]

        # print(self._preSum)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self._preSum[row2][col2] - (self._preSum[row2][col1 - 1] + self._preSum[row1 - 1][col2] - self._preSum[row1 - 1][col1 - 1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)