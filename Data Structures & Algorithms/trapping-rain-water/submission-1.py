class Solution:
    def trap(self, height: List[int]) -> int:
        # water=0
        # for i in range(len(height)):
        #     lefmax=max(height[:i+1])
        #     rightmax=max(height[i:])
        #     water+=(min(lefmax,rightmax)-height[i])
        # return water
        i=0
        j=len(height)-1
        water=0
        leftmax=0
        rightmax=0
        while(i<j):
            if(height[i]<=height[j]):
                if(height[i]<leftmax):
                    water+=(leftmax-height[i])
                else:
                    leftmax=height[i]
                i+=1
            else:
                if(height[j]<rightmax):
                    water+=(rightmax-height[j])
                else:
                    rightmax=height[j]
                j-=1
            
        return water