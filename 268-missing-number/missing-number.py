class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_sum = len(nums)
        for i in range(len(nums)):
            full_sum += i
            full_sum -= nums[i]
        return full_sum

