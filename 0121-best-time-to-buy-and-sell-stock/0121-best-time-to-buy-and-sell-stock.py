class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_prof = 0 
        min_price = prices[0]
        
        for i in range(1,len(prices)):
            max_prof = max(max_prof,prices[i] - min_price)
            min_price = min(min_price,prices[i])
            
            
        return max_prof