class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = float("-inf")
        sum = 0
        for i in nums:
            sum += i
            sum = max(i,sum)
            max_sum = max(sum,max_sum)
            
        return max_sum