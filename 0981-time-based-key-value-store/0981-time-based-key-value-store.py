class TimeMap:

    def __init__(self):
        self.tmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append([value,timestamp])
            
    def get(self, key: str, timestamp: int) -> str:
        for i in range(len(self.tmap[key])-1,-1,-1):
            v, t=self.tmap[key][i]
            if t<=timestamp:
                return v
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)