class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cash = 0
        stock = -prices[0]

        for i in range(1, n):
            cash, stock = max(stock + prices[i], cash), max(cash - prices[i], stock)     
        return cash