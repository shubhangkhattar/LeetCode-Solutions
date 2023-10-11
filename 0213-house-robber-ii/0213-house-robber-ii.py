
class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robber_1(nums[:-1]),self.robber_1(nums[1:]))


    def robber_1(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0

        for num in nums:
            rob1, rob2 =  rob2, max(rob2,rob1+num) 

        return rob2




