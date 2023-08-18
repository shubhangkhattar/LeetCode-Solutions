class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums)-1
        left = 0
        min_number = nums[0]
        while left <= right:
            if (nums[left] < nums[right]):
                return min(nums[left],min_number)

            middle = (left+right)//2
            min_number = min(nums[middle], min_number)

            if (nums[middle] >= nums[left]):
                left = middle+1
            else:
                right = middle-1

        return min_number