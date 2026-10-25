class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxl=0
        string=""
        for i in range(len(s)):
            left=i
            right=i
            str2=""
            while(left>=0 and right<len(s) and s[left]==s[right]):
                str2=s[left:right+1]
                if(maxl<len(str2)):
                    maxl=len(str2)
                    string=str2
                left-=1
                right+=1
        for i in range(len(s)):
            left=i
            right=i+1
            str2=""
            while(left>=0 and right<len(s) and s[left]==s[right]):
                str2=s[left:right+1]
                if(maxl<len(str2)):
                    maxl=len(str2)
                    string=str2
                left-=1
                right+=1
        return string
