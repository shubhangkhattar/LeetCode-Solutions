class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =  [amount+1] * (amount + 1)
        dp[0] = 0

        for total in range(1,amount + 1):
            for coin in coins:
                if total - coin >= 0:
                    dp[total] = min(dp[total],dp[total-coin] + 1)

        return dp[amount] if dp[amount] != amount+1 else -1