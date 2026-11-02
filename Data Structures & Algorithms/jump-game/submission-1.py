class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        for i in range(len(nums)):
            
            if(i>maxi):
                return False
            curr=i+nums[i]
            maxi=max(maxi,curr)
        
        return True