class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prefix = 1
        postfix = 1
        max_product = float("-inf")
        for i in range(len(nums)):
            j = len(nums) - 1 -i
            if prefix == 0:
                prefix = 1
            if postfix == 0:
                postfix = 1

            prefix = prefix * nums[i]
            postfix = postfix * nums[j]
            
            max_product = max(max_product,prefix,postfix)

        return max_product
            