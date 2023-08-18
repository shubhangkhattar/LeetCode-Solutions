class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_left = 0
        for right in range(1,len(prices)):
            current_profit = prices[right]-prices[min_left]
            max_profit = max(current_profit,max_profit)
            if prices[min_left] > prices[right]:
                min_left = right

        return max_profit