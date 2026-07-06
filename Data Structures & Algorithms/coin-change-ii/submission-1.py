class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            cur = dp[:]
    
            for j in range(coins[i], amount + 1):
                cur[j] = dp[j] + cur[j - coins[i]]

            dp = cur
        return dp[-1]