class TimeMap:

    def __init__(self):
        self.tmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append([value,timestamp])
            
    def get(self, key: str, timestamp: int) -> str:
        start=0
        end=len(self.tmap[key])-1
        if self.tmap[key] == []:
            return ''
        if self.tmap[key][0][1]>timestamp:
            return ''
        else:
            while start<=end:
                mid=(start+end)//2

                if self.tmap[key][mid][1]==timestamp:
                    return self.tmap[key][mid][0]
                elif self.tmap[key][mid][1]>timestamp:
                    end=mid-1
                else:
                    start=mid+1
            if self.tmap[key][mid][1]<=timestamp:
                return self.tmap[key][mid][0]
            else:
                if self.tmap[key][mid-1][0] is None:
                    return ''
                else:
                    return self.tmap[key][mid-1][0]
        
    
        # for v, t in self.tmap[key]:
        #     if t>timestamp:
        #         break
        #     else:
        #         answer=v
        # return answer


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)