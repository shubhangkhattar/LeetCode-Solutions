class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums.copy()
        print(dp)
        for i in range(len(nums)):
            if (i-1) > 0:
                print(i)
                dp[i] += max(dp[0:i-1])

        return max(dp)

                

