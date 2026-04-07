class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[0][0]:
            return 0
        if ROW == 1:
            if sum(obstacleGrid[0]) == 0:
                return 1
            else:
                return 0
        
        preRow = [1] * COL
        for i in range(COL-2, -1, -1):
            if obstacleGrid[ROW-1][i] == 1:
                preRow[i] = 0
            else:
                preRow[i] = preRow[i+1]
        lastColBlocked = False
        for i in range(ROW-2, -1, -1):
            curRow = [0] * COL
            if obstacleGrid[i][COL-1] == 1:
                lastColBlocked = True
            curRow[-1] = 0 if lastColBlocked else 1
            for j in range(COL-2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    curRow[j] = curRow[j+1] + preRow[j]
                else:
                    curRow[j] = 0
            preRow = curRow
        
        return curRow[0]