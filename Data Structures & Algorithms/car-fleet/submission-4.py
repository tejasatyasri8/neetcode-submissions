class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        # stack=[]
        # for p,s in pair:
        #     stack.append((target-p)/s)
        #     if len(stack)>=2 and stack[-1]<=stack[-2]:
        #         stack.pop()
        # return len(stack)

        fleet=1
        prevtime=((target-pair[0][0])/pair[0][1])
        for i in range(1,len(pair)):
            curtime=((target-pair[i][0])/pair[i][1])
            if curtime>prevtime:
                fleet+=1
                prevtime=curtime
        return fleet
            


            
        # 7 4 1 0  1 1.5  6 2.5 5 
        # 1 2 2 1

        # 3 3 4.5 10