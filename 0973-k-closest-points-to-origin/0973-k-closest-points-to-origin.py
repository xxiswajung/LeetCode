class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hash={}
        ans=[]
        res=[]
        for i in range(len(points)):
            length=int(math.pow(points[i][0],2)+math.pow(points[i][1],2))
            ans.append((i,length))
        ans.sort(key=lambda x:x[1])
        
        i=0
        while k!=0:
            res.append(points[ans[i][0]])
            i+=1
            k-=1
        return res
