class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()

        nums.sort()
        n = len(nums)
        for i in range(0, n - 2):

            left = i + 1
            right = n - 1

            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    result.add((nums[i], nums[left], nums[right]))
                if -nums[i] < (nums[left] + nums[right]):
                    right -= 1
                else:
                    left += 1
        return list(result)