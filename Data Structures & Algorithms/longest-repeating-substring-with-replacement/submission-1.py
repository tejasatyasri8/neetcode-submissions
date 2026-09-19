class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # res=0
        # for i in range(len(s)):
        #     dict1={}
        #     maxf=0
        #     for j in range(i,len(s)):
        #         dict1[s[j]]=dict1.get(s[j],0)+1
        #         maxf=max(maxf,dict1[s[j]])
        #         if ((j-i+1)-maxf)<=k:
        #             res=max(res,j-i+1)
        # return res
        i=0
        j=0
        maxlen=0
        maxf=0
        dict1={}
        while(j<len(s)):
            dict1[s[j]]=dict1.get(s[j],0)+1
            length=j-i+1
            maxf=max(maxf,dict1[s[j]])
            if(length-maxf)<=k:
                maxlen=max(length,maxlen)
            else:
                while (j-i+1)-maxf>k:
                    dict1[s[i]]-=1
                    i+=1
            j+=1
        return maxlen




