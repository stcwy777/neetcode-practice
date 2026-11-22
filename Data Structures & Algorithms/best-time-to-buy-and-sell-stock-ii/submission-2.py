class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cash = 0
        stock = -prices[0]

        for i in range(1, n):
            # cash
            cash = max(stock + prices[i], cash)
            # stock
            stock = max(cash - prices[i], stock)

            # cash = new_cash
            # stock = new_stock        
        return cash