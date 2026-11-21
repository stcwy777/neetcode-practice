class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p = [-prices[0]] * n
        q = [0] * n

        for i in range(1, n):
            # own
            p[i] = max(q[i - 1] - prices[i], p[i - 1])
            # not own
            q[i] = max(q[i - 1], p[i - 1] + prices[i])
        
        return q[n - 1]