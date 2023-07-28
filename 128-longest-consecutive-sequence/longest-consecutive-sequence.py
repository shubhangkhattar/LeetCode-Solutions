class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0

        nums.sort()

        last_min = -float('inf')

        current_max = 0

        max_count = 1


        for num in nums:
            if num-1 == last_min:
                current_max += 1
                max_count = max(current_max,max_count)
                last_min = num
                continue

            if num != last_min:
                current_max = 1
                last_min = num

        return max_count