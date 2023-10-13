class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_count = 0

        for i in nums:
            count = 1
            if i-1 not in nums:
                while i+1 in nums:
                    count += 1
                    i += 1

            max_count = max(max_count,count)

        return max_count
