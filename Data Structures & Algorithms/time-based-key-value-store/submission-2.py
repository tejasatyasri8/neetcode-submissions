class TimeMap:

    def __init__(self):
        self.keystore={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key]={}
        if timestamp not in self.keystore[key]:
            self.keystore[key][timestamp]=[]
        self.keystore[key][timestamp].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore:
            return ""
        # seen=-1
        # for time in self.keystore[key]:
        #     if time<=timestamp:
        #         seen=max(seen,time)
        # return "" if seen==-1 else self.keystore[key][seen][-1]
        timestamps=list(self.keystore[key].keys())
        l=0
        r=len(timestamps)-1
        res=""
        while(l<=r):
            m=(l+r)//2
            if timestamps[m]<=timestamp:
                res=self.keystore[key][timestamps[m]]
                l=m+1
            else:
                r=m-1
        return res[-1] if res else ""








        