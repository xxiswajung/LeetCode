class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph=[[0]*(numCourses) for _ in range(numCourses)]
#         degree=[0]*(numCourses)
#         Q=deque()
        
#         for i in range(len(prerequisites)):
#             x=prerequisites[i][0]
#             y=prerequisites[i][1]
#             graph[x][y]=1
#             degree[y]+=1
#         for i in range(numCourses):
#             if degree[i]==0:
#                 Q.append(i)
#         if len(Q)==0:
#             return False
        
#         while Q:
#             item=Q.popleft()
#             for i in range(numCourses):
#                 if graph[item][i]==1:
#                     degree[i]-=1
#                     if degree[i]==0:
#                         Q.append(i)
#         if sum(degree)==0:
#             return True
#         else:
#             return False

        graph = [[] for _ in range(numCourses)]
        traced, visited = set(), set()
        for x, y in prerequisites:
            graph[x].append(y) #x의 선수과목 y들 저장
            
        def dfs(i): 
            if i in traced:
                return False
            if i in visited:
                return True
            traced.add(i) #graph[i]가 빈 경우 = 선수과목이 없는 경우 -? 실행 x, True
        
            #선수과목 불러옴, 반복하면서 traced에 남아있으면 False
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True
    
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True