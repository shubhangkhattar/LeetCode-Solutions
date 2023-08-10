class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = -100000000
        prefix = 1
        suffix = 1
        n = len(nums)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]
            max_product = max(max_product,prefix,suffix)

        return max_product

        