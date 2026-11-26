class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        ds=[""]*(n*2)
        def pa(idx,total,ds):
            if(idx==(n*2)):
                if(total==0):
                    res.append("".join(ds))
                return
            if(total<0):
                return
            elif(total>(len(ds)//2)):
                return
            ds[idx]="("
            pa(idx+1,total+1,ds)
            ds[idx]=")"
            pa(idx+1,total-1,ds)
        pa(0,0,ds)
        return res


