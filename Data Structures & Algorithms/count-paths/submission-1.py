class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # last row all 1:
        if m < 2:
            return 1
        prev_row = [1] * n
        for i in range(m - 2, -1, -1):
            cur_row = [0] * n
            cur_row[n-1] = 1
            for j in range(n - 2, -1, -1):
                cur_row[j] = cur_row[j+1] + prev_row[j]
            prev_row = cur_row
        return cur_row[0]