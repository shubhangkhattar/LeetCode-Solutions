class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        pre = 1
        post = 1
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        for i in range(len(nums)):
            prefix[i] = pre * nums[i]
            pre = prefix[i]
            postfix[len(nums) - 1 - i] = post * nums[len(nums) - 1 - i]
            post = postfix[len(nums) - 1 - i]
            
        print(prefix)
        print(postfix)
        output = []
        output.append(postfix[1])
        for i in range(1,len(nums)-1):
            print(i)
            output.append(prefix[i-1] * postfix[i+1])
        output.append(prefix[len(nums)-2])
        
        return output