class Solution:
    def twoSum(self, numbers, target):
        i = 0;
        j = len(numbers)-1

        while(i<j):
            num_i = numbers[i]
            num_j = numbers[j]
            sum = num_i + num_j
            if(sum == target):
                return [i+1,j+1]
            else:
                if(sum>target):
                    j -= 1
                else:
                    i += 1

