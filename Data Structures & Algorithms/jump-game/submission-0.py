class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        for i in range(len(nums)):
            curr=i+nums[i]
            
            if(i>maxi):
                return False
            maxi=max(maxi,curr)
        
        return True