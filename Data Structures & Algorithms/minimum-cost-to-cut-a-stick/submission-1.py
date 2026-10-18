class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        
        dp = [[0] * m for _ in range(m)]

        for l in range(m - 3, -1, -1):
            for r in range(l + 2, m):
                dp[l][r] = float('INF')
                for k in range(l + 1, r):
                    dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r] + cuts[r] - cuts[l])

        return dp[0][m - 1]
