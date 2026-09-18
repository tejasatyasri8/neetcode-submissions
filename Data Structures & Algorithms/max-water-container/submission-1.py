class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max1=0
        # for i in range(len(heights)):
        #     for j in range(i,len(heights)):
        #         breadth=j-i
        #         heigh=min(heights[i],heights[j])
        #         count=breadth*heigh
        #         max1=max(count,max1)
        # return max1
        maxl=0
        i=0
        j=len(heights)-1
        while(i<j):
            area=(j-i)*(min(heights[i],heights[j]))
            maxl=max(maxl,area)
            if(heights[i]<heights[j]):
                i+=1
            else:
                j-=1
        return maxl
