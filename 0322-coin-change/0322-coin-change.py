class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp_array = (amount+1) * [amount+1]
        dp_array[0] = 0
        
        for total in range(1,amount+1):
            for coin in coins:
                if total >= coin:
                    dp_array[total] = min(dp_array[total],dp_array[total-coin] + 1)
        
        return dp_array[amount] if dp_array[amount] != amount+1 else -1