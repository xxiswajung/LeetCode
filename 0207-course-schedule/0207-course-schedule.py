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

        graph = [[] for _ in range(numCourses)] #강의 수강 후 들을 수 있는 강의리스트
        traced, visited = set(), set()
        for x, y in prerequisites:
            graph[x].append(y) #x의 선수과목 y들 저장
            
        def dfs(i): 
            #순환 구조면 False
            if i in traced:
                return False
            #이미 방문했던 노드면 True (=완전히 탐색이 끝난 코드)
            if i in visited:
                return True
            #traced에도 없고 visited에도 없다면 traced에 추가해줌
            traced.add(i) 
        
            #선수과목 불러옴, 반복하면서 traced에 남아있으면 False
            for y in graph[i]:
                if not dfs(y): #이미 방문한 적이 있는 경우
                    return False
            #탐색 종료 후 순한노드 삭제
            traced.remove(i)
            #탐색 종료 후 방문노드 추가
            visited.add(i)
            return True
    
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True