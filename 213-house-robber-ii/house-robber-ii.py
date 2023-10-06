
class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robber_1(nums[:-1]),self.robber_1(nums[1:]))
        
    def robber_1(self, nums: List[int]) -> int:
        rob_1, rob_2 = 0,0

        for n in nums:
            temp = max(n+rob_1,rob_2)
            rob_1 = rob_2
            rob_2 = temp

        return rob_2





