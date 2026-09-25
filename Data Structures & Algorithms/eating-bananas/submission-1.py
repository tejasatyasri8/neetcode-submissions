from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # m=max(piles)
        # k=1
        # if(h==len(piles)):
        #     return m
        # else:
        #     while(k<m):
        #         noofhours=0
        #         for i in range(len(piles)):
        #             noofhours+=(ceil(piles[i]/k))
        #         if noofhours<=h :
        #             return k
        #         k+=1
        
        l=1
        r=max(piles)
        res=r
        while(l<=r):
            mid=(l+r)//2
            noofhours=0
            for i in range(len(piles)):
                noofhours+=(ceil(piles[i]/mid))
            if(noofhours<=h):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res

                    