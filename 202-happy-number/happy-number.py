class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while True:
            happy_calc = 0
            while n > 0:
                one = n%10
                n = n//10
                happy_calc += one**2
            if happy_calc == 1:
                return True
            if happy_calc in visit:
                return False
            visit.add(happy_calc)
            n = happy_calc
            




    