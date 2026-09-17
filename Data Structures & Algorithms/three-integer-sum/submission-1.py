class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # seen=set()
        # for i in range(len(nums)):
        #     j=i+1
        #     dict1={}
        #     while(j<len(nums)):
        #         needed=-(nums[i]+nums[j])
        #         if(needed in dict1):
        #             list1=[nums[i],nums[j],needed]
        #             sortedl=tuple(sorted(list1))
        #             seen.add(sortedl)
        #         dict1[nums[j]]=j
        #         j+=1
        # return list(seen)
        sortedl=sorted(nums)
        seen=set()
        for i in range(len(nums)):
            j=i+1
            last_int=sortedl[0]
            dict1={}
            while(j<len(sortedl)):
                needed=-(sortedl[i]+sortedl[j])
                if needed in dict1:
                    seen.add(tuple([sortedl[i],sortedl[j],needed]))
                dict1[sortedl[j]]=j
                j+=1
        return list(seen)                  
