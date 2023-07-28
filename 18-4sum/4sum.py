class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        
        result = set()
        


        for i in range(len(nums)-3):
            for j in range(i+3,len(nums)):
                target_dif = target - (nums[i] + nums[j])
                left = i+1
                right = j-1
                while left < right:
                    if nums[left] + nums[right] == target_dif:
                        result.add((nums[i],nums[left],nums[right],nums[j]))

                    if nums[left] + nums[right] > target_dif:
                        right -= 1
                    else :
                        left += 1
        return result

                    
            
            