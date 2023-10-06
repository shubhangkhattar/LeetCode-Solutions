class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == -a:
                    res.append([a, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                        continue
                if -a < sum:
                    r -= 1
                else:
                    l += 1
        

        return res

