class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum_1 = 0 
        max_1 = 0
        
        for num in nums:
            if num == 0:
                sum_1 = 0
            else:
                sum_1 += 1
                max_1 = max(sum_1,max_1)
                
        return max_1