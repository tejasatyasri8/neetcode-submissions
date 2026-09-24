class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        m=int(len(nums)/2)
        while(l<=r):
            if(nums[m]==target):
                return m
            elif(nums[m]<target):
                l=m+1
            elif(nums[m]>target):
                r=m-1
            m=int((r+l)/2)
        return -1
        
            
