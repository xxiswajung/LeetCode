class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Solve by DFS
        preMap={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited=set()
        
        def DFS(crs):
            if crs in visited:
                return False
            if preMap[crs]==[]:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not DFS(pre):
                    return False
            #remove from the set() : If src remained in set, then it causes false when crs encounter the 'if crs in visited' and return False even if the preMap doesn't have a cycle.
            visited.remove(crs)
            #Also erase already taken courses from the crs dict
            preMap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not DFS(crs):
                return False
        return True
        
        
        
#         graph=[[0]*numCourses for _ in range (numCourses)]
#         degree=[0]*numCourses
#         Q=deque()
        
#         for i in range(len(prerequisites)):
#             a=prerequisites[i][0]
#             b=prerequisites[i][1]
#             graph[a][b]=1
#             degree[b]+=1
#         for i in range(numCourses):
#             if degree[i]==0:
#                 Q.append(i)
#         if len(Q)==0:
#             return False
        
#         while Q:
#             x=Q.popleft()
#             for i in range(numCourses):
#                 if graph[x][i]==1:
#                     degree[i]-=1
#                     if degree[i]==0:
#                         Q.append(i)
        
#         if sum(degree)==0:
#             return True