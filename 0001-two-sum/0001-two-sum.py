class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_map = dict()

        for i in range(len(nums)):
            dif = target-nums[i]
            if dif in hash_map:
                return([hash_map[dif],i])
            hash_map[nums[i]] = i
