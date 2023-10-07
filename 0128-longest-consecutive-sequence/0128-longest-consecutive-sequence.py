class Solution(object):
    def longestConsecutive(self, nums):
        
        numSet = set(nums)
        max_count = 0
        
        for num in numSet:
            if num-1 not in numSet:
                current_num = num
                count = 0
                while current_num in numSet:
                    count+=1
                    current_num = current_num+1
                max_count = max(max_count,count)
                 
        return max_count