class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        element = None
        count = 0

        for i in nums:
            if count == 0:
                element = i
                count = 1
                continue

            if element == i:
                count += 1
            else:
                count -= 1
            
        return element
            
