class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        DP_Array = [1]*len(nums)
        maximum_length = 1

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    DP_Array[i] = max(DP_Array[j]+1,DP_Array[i])

        return max(DP_Array)