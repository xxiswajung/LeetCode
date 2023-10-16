class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #using BFS
        m=len(mat)
        n=len(mat[0])
        Q=deque()
        
        for i, row in enumerate(mat):
            for j, element in enumerate(row):
                if element: #1들을 무한대로 초기화 하기
                    mat[i][j] = float('inf')
                else: #0들은 deque에 쌓기
                    Q.append((i,j))
        
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        
        while Q:
            for k in range(len(Q)):
                i, j = Q.popleft()
                for t in range(4):
                    xx=i+dx[t]
                    yy=j+dy[t]
                    if 0<=xx<m and 0<=yy<n and mat[xx][yy]>mat[i][j]+1: #초기:무한대로 초기화했으니 당연 -> 중반:0과의 거리를 기록한 cell들로 기록을 이어받을 수 있음
                        mat[xx][yy]=mat[i][j]+1
                        Q.append((xx,yy))
        return mat
    
#         #using DP
#         m=len(mat)
#         n=len(mat[0])
        
#         for i, row in enumerate(mat):
#             for j, element in enumerate(row):
#                 if element:
#                     top=mat[i-1][j]+1 if i>0 else float('inf')
#                     left=mat[i][j-1]+1 if j>0 else float('inf')
#                     mat[i][j]=min(top,left)
        
#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 element=mat[i][j]
#                 if element:
#                     bottom=mat[i+1][j]+1 if i<m-1 else float('inf')
#                     right=mat[i][j+1]+1 if j<n-1 else float('inf')
#                     mat[i][j]=min(element,bottom,right)
        
#         return mat
