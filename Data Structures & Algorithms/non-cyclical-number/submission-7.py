class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while (n!=1):
            n=self.sumofsquare(n)
            if n in visit:
                return False
            visit.add(n)
        return True
    def sumofsquare(self, num : int) -> int:
        square=0
        while num!=0:
            x=num%10
            square+=x**2
            num=num//10
            print(square)
        return square

        