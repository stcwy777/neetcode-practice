class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        bag = max(days)
        dp = [float('inf')] * (bag + 1)
        dp[0] = 0

        for i in range(1, bag + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
        
        return dp[-1]