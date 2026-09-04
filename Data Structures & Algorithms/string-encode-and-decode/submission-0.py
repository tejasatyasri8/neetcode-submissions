class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_s=""
        for s in strs:
            encoded_s+=str(len(s))+"#"+s
        return encoded_s
    def decode(self, s: str) -> List[str]:
        decoded_s=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!="#"):
                j+=1
            length=int(s[i:j])
            i=j+1
            decoded_s.append(s[i:i+length])
            i+=length
        return decoded_s