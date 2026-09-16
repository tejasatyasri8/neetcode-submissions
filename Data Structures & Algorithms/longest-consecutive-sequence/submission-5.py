class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        # nums.sort()
        # cnt=1
        # larg=1
        # last_sml=nums[0]
        # for i in range(1,len(nums)):
        #     if(nums[i]==last_sml+1):
        #         cnt+=1
        #         last_sml=nums[i]
        #     elif(nums[i]==last_sml):
        #         continue
        #     else:
        #         last_sml=nums[i]
        #         cnt=1
        #     larg=max(cnt,larg)
        # return larg
        cnt=1
        large=1
        seen=set()
        for i in range(len(nums)):
            seen.add(nums[i])
        for num in seen:
            if(num-1 not in seen):
                x=num
                while x+1 in seen:
                    x+=1
                    cnt+=1
            
            large=max(cnt,large)
            cnt=1
        return large
