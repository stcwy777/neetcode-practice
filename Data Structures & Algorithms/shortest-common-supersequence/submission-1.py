class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N1, N2 = len(str1), len(str2)

        dp = []
        for i in range(N2 + 1):
            dp.append(str2[:i])

        for i in range(1, N1 + 1):
            cur = [''] * (N2 + 1)
            cur[0] = str1[:i]

            for j in range(1, N2 + 1):
                c1 = str1[i - 1]
                c2 = str2[j - 1]
                if c1 == c2:
                    cur[j] = dp[j - 1] + c1
                else:
                    if len(dp[j]) < len(cur[j - 1]):
                        cur[j] = dp[j] + c1
                    else:
                        cur[j] = cur[j - 1] + c2

            dp = cur

        return dp[-1]