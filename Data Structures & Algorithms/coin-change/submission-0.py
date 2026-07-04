class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(N):
            cur = dp[:]
            for j in range(coins[i], amount + 1):
                cur[j] = min(dp[j], cur[j - coins[i]] + 1)
            dp = cur
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]