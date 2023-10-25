class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[0]*(numCourses) for _ in range(numCourses)]
        degree=[0]*(numCourses)
        Q=deque()
        
        for i in range(len(prerequisites)):
            x=prerequisites[i][0]
            y=prerequisites[i][1]
            graph[x][y]=1
            degree[y]+=1
        for i in range(numCourses):
            if degree[i]==0:
                Q.append(i)
        
        while Q:
            item=Q.popleft()
            for i in range(numCourses):
                if graph[item][i]==1:
                    degree[i]-=1
                    if degree[i]==0:
                        Q.append(i)
        if sum(degree)==0:
            return True
        else:
            return False