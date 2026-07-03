class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)

        # dp[m][n]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            cur = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    zeros = s.count('0')
                    ones = s.count('1')
                    if i >= zeros and j >= ones:
                        cur[i][j] = max(dp[i - zeros][j - ones] + 1, dp[i][j])
                    else:
                        cur[i][j] = dp[i][j]
            dp = cur
        
        return cur[m][n]