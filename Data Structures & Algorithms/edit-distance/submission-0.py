class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)

        dp = list(range(l2 + 1))


        for i in range(1, l1 + 1):
            cur = [i] * (l2 + 1)
            for j in range(1, l2 + 1):
                w1, w2 = word1[i - 1], word2[j - 1]
                if w1 == w2:
                    cur[j] = dp[j - 1]
                else:
                    cur[j] = min(dp[j - 1], dp[j], cur[j - 1]) + 1
            dp = cur
        return dp[-1]