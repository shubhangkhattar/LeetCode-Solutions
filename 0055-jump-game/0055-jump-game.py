class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            ans = False
            if i + nums[i] >= goal:
                goal = i
                ans = True
        
        return ans
