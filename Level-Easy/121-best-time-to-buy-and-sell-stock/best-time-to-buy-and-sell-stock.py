class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = 0
        second = 1
        maxProfit = 0
        while second < len(prices):
            if prices[first] > prices[second]:
                first = second
            else:
                maxProfit = max(maxProfit, prices[second] - prices[first])
            second += 1
        return maxProfit
