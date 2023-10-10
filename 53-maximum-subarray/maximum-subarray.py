class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = nums[0]
        for num in nums[1:]:
            sum = max(sum+num,num)
            max_sum = max(sum,max_sum)
            
        
        return max_sum