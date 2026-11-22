class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set1=set()
        
        for i in range(len(nums)):
            x=nums[i]
            if x not in set1:
                set1.add(x)
            else:
                return x