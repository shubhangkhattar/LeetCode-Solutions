class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        for i in range(n):
            one,two = one + two,one
            
        return two