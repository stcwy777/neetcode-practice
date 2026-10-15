class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        pre = [0] * 3
        pre[0] = -prices[0]
        # 0: have coin, 1: no coin: sold, 2: no coin do nothing
        for i in range(1, n):
            cur = pre[:]
            cur[0] = max(pre[2] - prices[i], pre[0])
            cur[1] = pre[0] + prices[i]
            cur[2] = max(pre[1], pre[2])

            pre = cur[:]
        
        return max(pre[1], pre[2])

