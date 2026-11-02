class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        sum1=0
        maxi=float('-inf')
        while(i<len(nums)):
            sum1+=nums[i]
            maxi=max(sum1,maxi)
            if(sum1<0):
                sum1=0
            i+=1
        return maxi

