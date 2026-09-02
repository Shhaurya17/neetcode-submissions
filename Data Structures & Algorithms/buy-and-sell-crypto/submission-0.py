class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=101
        profit=0
        for i in range(1,len(prices)):
            mini = min(prices[i-1],mini)
            currprofit = prices[i]- mini
            if profit <= currprofit:
                profit = currprofit
        return profit