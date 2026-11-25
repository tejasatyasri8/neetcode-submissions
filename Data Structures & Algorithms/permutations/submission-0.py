class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        freq=[0 for _ in range(len(nums))]
        ds=[]
        ans=[]
        def cs(ds,freq):
            if(len(ds)==len(nums)):
                ans.append(ds.copy())
                return
            for i in range(len(nums)):
                if freq[i]!=1:
                    freq[i]=1
                    ds.append(nums[i])
                    cs(ds,freq)
                    freq[i]=0
                    ds.remove(nums[i])
        cs(ds,freq)
        return ans


