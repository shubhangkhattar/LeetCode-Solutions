class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        if len(nums) > 1: 
            pivot = self.findPeak(nums) - 1 if self.findPeak(nums) else -1
            if pivot != -1:
                nextInd = self.findNext(nums, pivot)
                nums[nextInd], nums[pivot] = nums[pivot], nums[nextInd]
            self.reverse(nums, pivot+1)  
        #reverse the second half; reverse whole array if it's [3,2,1], which means pivot = -1

    def findPeak(self, nums):
        for i in range(len(nums))[::-1]:
            if nums[i-1] < nums[i]:
                return i
            
    def findNext(self, nums, p):
        for i in range(p+1,len(nums))[::-1]:
            if nums[i]>nums[p]:
                return i
            
    def reverse(self, nums, start):
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1