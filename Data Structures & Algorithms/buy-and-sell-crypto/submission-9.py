class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprofit = 0

        while r <= len(prices) - 1:
            if prices[r] > prices[l]:
                maxprofit = max(maxprofit, (prices[r] - prices[l]))
                r+=1
            else:
                l = r
                r = l + 1
        return maxprofit            
        