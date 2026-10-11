class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1=[]
        num=0
        x=len(digits)-1
        for i in range(len(digits)):
            num+=(digits[i]*(10**x))
            x-=1
        num+=1
        while(num!=0):
            list1.append(num%10)
            num=num//10
        list1.reverse()
        return list1