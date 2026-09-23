class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        list1=[0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     count=0
        #     for j in range(i+1,len(temperatures)):
        #         count+=1
        #         if(temperatures[j]>temperatures[i]):
        #             list1[i]+=count
        #             break
        # return list1
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                stackT,stackind=stack.pop()
                list1[stackind]=i-stackind
            stack.append([temperatures[i],i])
        return list1

            

