class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)

        if N1 + N2 != N3:
            return False
        
        dp = [[False] * (N2 + 1) for _ in range(N1 + 1)]
        dp[0][0] = True

        for i in range(1, N1 + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])

        for j in range(1, N2 + 1):
            dp[0][j] = (dp[0][j - 1] and s2[j - 1] == s3[j - 1])

        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                from_s1 = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                from_s2 = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

                dp[i][j] = from_s1 or from_s2
        
        return dp[N1][N2]