class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)

        dp =  [0] * (n2 + 1) 
        dp[0] = 1

        for i in range(n1):
            cur = [0] * (n2 + 1)
            cur[0] = 1
            for j in range(1, n2 + 1):

                if s[i] == t[j - 1]:
                    cur[j] = dp[j - 1] + dp[j]
                else:
                    cur[j] = dp[j]
            dp = cur
        
        return dp[-1]