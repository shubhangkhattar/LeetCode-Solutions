class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        
        max_count = 0
        
        for num in nums:
            count = 1
            if num-1 not in nums:
                current_num = num
                while current_num + 1 in nums:
                    current_num += 1
                    count += 1
            max_count = max(max_count,count)
                    
        return max_count
            