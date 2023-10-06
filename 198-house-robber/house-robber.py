class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_1, rob_2 = 0,0
        
        for n in nums:
            temp = max(n+rob_1,rob_2)
            rob_1 = rob_2
            rob_2 = temp
        
        return rob_2
            