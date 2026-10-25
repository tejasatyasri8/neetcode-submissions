class Solution:
    def numDecodings(self, s: str) -> int:
        memo=[0]*(len(s)+1)
        # def dp(i):
        #     if(i==len(s)):
        #         return 1
        #     if(s[i]=='0'):
        #         return 0
        #     if(memo[i]!=-1):
        #         return memo[i]
        #     ways=dp(i+1)
        #     if(i+1<len(s) and 10<=int(s[i:i+2])<=26):
        #         ways+=dp(i+2)
        #     memo[i]=ways
        #     return memo[i]
        # return dp(0)
        n=len(s)
        memo[n]=1
        for i in range(len(s)-1,-1,-1):
            ways=0
            if(s[i]=='0'):
                memo[i]=0
            else:
                ways=memo[i+1]
                if(i+1<len(s) and 10<=int(s[i:i+2])<=26):
                    ways+=memo[i+2]
                memo[i]=ways
        return memo[0]
            