class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)
        
        if rootX!=rootY:
            if self.rank[rootX]>self.rank[rootY]:
                self.parent[rootY]=rootX
            elif self.rank[rootX]<self.rank[rootY]:
                self.parent[rootX]=rootY
            else:
                self.parent[rootY]=rootX
                self.rank[rootX]+=1
                
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf=UnionFind(n)
        logs.sort()
        
        for time,x,y in logs:
            uf.union(x,y)
            if all(uf.find(i)==uf.find(0) for i in range(n)):
                return time
        return -1
#         logs.sort()
#         visited=[]
#         small_group=[]
#         for timestamp, p1, p2 in logs:
#             tmp=set()

#             if p1 not in visited and p2 not in visited:
#                 visited.append(p1)
#                 visited.append(p2)
#                 tmp.add(p1)
#                 tmp.add(p2)
#                 small_group.append(tmp)
#             elif p1 in visited and p2 not in visited:
#                 visited.append(p2)
#                 for item in small_group:
#                     if p1 in item:
#                         item.add(p2)
#             elif p1 not in visited and p2 in visited:
#                 visited.append(p1)
#                 for item in small_group:
#                     if p2 in item:
#                         item.add(p1)
#             else:
#                 for item in small_group:
#                     if p1 in item:
#                         a1=item
#                     if p2 in item:
#                         a2=item
#                 small_group.append(a1.union(a2))
#                 small_group.remove(a1)
                
#             if {i for i in range(n)} in small_group:
#                 return timestamp
#         return -1
       
            