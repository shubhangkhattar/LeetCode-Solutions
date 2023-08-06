class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        n = len(nums)

        def compute_subset(index, subset):
            if index == n:
                ans.append(subset)
                return

            out1 = subset[:]
            subset.append(nums[index])
            out2 = subset[:]

            compute_subset(index+1,out1)
            compute_subset(index+1,out2)

        compute_subset(0,[])
        return ans


print(Solution().subsets([1,2,3]))
