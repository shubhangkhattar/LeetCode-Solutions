class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        count_1 = 0
        element_1 = None

        count_2 = 0
        element_2 = None


        for num in nums:

            if count_1 == 0 and num != element_2 :
                element_1 = num
                count_1 = 1
            elif count_2 == 0 and num != element_1:
                element_2 = num
                count_2 = 1
            elif element_1 == num:
                count_1 += 1
            elif element_2 == num:
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1

        count_1, count_2 = 0, 0

        for num in nums:
            if num == element_1:
                count_1 += 1
            if num == element_2:
                count_2 += 1

        min_count = len(nums)//3 + 1
        result = []

        if count_1 >= min_count:
            result.append(element_1)
        if count_2 >= min_count:
            result.append(element_2)
        return (result)