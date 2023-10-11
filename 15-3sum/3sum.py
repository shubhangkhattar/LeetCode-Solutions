class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            outer_sum = -1*nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                inner_sum = nums[left] + nums[right]
                if outer_sum == inner_sum:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while left < len(nums)-1 and nums[left] == nums[left-1]:
                        left += 1           
                elif outer_sum < inner_sum:
                    right -= 1
                else:
                    left += 1

        return result

# [-1,-1,0,1]

        
