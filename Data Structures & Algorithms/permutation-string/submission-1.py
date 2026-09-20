class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # s1=sorted(s1)
        # for i in range(len(s2)):
        #     str1=""
        #     for j in range(i,len(s2)):
        #         str1+=s2[j]
        #         if(s1==sorted(str1)):
        #             return True
        # return False
        dict1={}
        for i in range(len(s1)):
           dict1[s1[i]]=dict1.get(s1[i],0)+1
        
        # for i in range(len(s2)):
        #     dict2={}
        #     for j in range(i,len(s2)):
        #         if s2[j] not in dict1.keys():
        #             break
        #         if(s2[j] in dict1.keys()):
        #             dict2[s2[j]]=dict2.get(s2[j],0)+1
        #             if(dict1==dict2):
        #                 return True
        # return False

        s1=sorted(s1)
        i = 0
        j = len(s1)

        while j <= len(s2):
            if s2[i] not in dict1:
                i += 1
                j += 1
                continue

            substr = s2[i:j]

            if sorted(substr) == s1:
                return True

            i += 1
            j += 1

        return False
        






















