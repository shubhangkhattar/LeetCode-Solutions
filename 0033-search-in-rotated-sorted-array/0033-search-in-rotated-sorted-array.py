class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle

            if (nums[middle] >= nums[left]):
                if (target > nums[middle]) or (target < nums[left]):
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if (target < nums[middle]) or (target > nums[right]):
                    right = middle - 1
                else:
                    left = middle + 1

        return -1