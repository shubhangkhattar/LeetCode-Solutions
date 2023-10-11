class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 :
            return False
        
        array = []

        while x > 0:
        
            val = x%10
            x = x//10
            array.append(val)

        return array[:] == array[::-1]