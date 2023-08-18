class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        sum = 0
        for i in nums:
            sum += i
            sum = max(sum,i)
            max_sum = max(max_sum,sum)

        return max_sum