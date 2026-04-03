class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            profit = prices[r] - prices[l]
            maxprofit = max(maxprofit, profit) 
        return maxprofit       

        