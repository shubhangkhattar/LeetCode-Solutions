class Solution:
    def climbStairs(self, n: int) -> int:
        first,two = 1,1

        for i in range(n-1):
            two,first = two + first, two
        
        return two