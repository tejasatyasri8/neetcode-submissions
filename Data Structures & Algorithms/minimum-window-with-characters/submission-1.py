class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)==0 or len(s)<len(t):
            return ""
        # dict1={}
        # for i in range(len(t)):
        #     dict1[t[i]]=dict1.get(t[i],0)+1
        # res=[-1,-1]
        # reslen=float("infinity")
        # for i in range(len(s)):
        #     dict2={}
        #     for j in range(i,len(s)):
        #         dict2[s[j]]=dict2.get(s[j],0)+1
        #         flag=True
        #         for c in dict1:
        #             if dict1[c]>dict2.get(c,0):
        #                 flag=False
        #                 break
        #         if flag and (j-i+1)<reslen:
        #             reslen=j-i+1
        #             res=[i,j]
        # l,r=res
        # return s[l:r+1] if reslen!=float("infinity") else ""
        dict1={}
        for i in range(len(t)):
            dict1[t[i]]=dict1.get(t[i],0)+1
        i=0
        j=0
        dict2={}
        reslen=float("infinity")
        res=[-1,-1]
        matches=0
        need=len(dict1)
        while(i<=j and j<len(s)):
            dict2[s[j]]=dict2.get(s[j],0)+1
            if(s[j] in dict1 and dict1[s[j]]==dict2[s[j]]):
                matches+=1
            
            while(matches==need):
                if (reslen>j-i+1):
                    reslen=min(reslen,j-i+1)
                    res=[i,j]
                dict2[s[i]]-=1
                if s[i] in dict1 and dict2[s[i]]<dict1[s[i]]:
                    matches-=1 
                i+=1
            j+=1
        l,r=res
        return s[l : r + 1] if reslen != float("infinity") else ""

            

                

