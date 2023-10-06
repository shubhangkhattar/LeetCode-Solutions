from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        minimum_number = nums[0]

        while left <= right:

            if(nums[left] < nums[right]):
                return min(nums[left],minimum_number)

            middle = left + (right - left)//2

            minimum_number = min(minimum_number,nums[middle])

            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1

        return minimum_number

