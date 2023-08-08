class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp_array = [0] * (amount+1)
        dp_array[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i],len(dp_array)):
                dp_array[j] += dp_array[j - coins[i]]


        return dp_array[amount]