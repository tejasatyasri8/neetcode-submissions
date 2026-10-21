class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref=1
        suff=1
        prod=float("-inf")
        for i in range(len(nums)):
            pref*=nums[i]
            prod=max(prod,pref)
            if(pref==0):
                pref=1
                
        for i in range(len(nums)-1,-1,-1):
            suff*=nums[i]
            prod=max(prod,suff)
            if(suff==0):
                suff=1

        return prod