class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl=0
        dict1={}
        l=0
        r=0
        while(r<len(s)):
            if(s[r] in dict1):
                l=max(dict1[s[r]]+1,l)
            leng=r-l+1
            maxl=max(leng,maxl)
            dict1[s[r]]=r
            r+=1
        return maxl