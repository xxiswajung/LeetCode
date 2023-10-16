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
                    if 0<=xx<m and 0<=yy<n and mat[xx][yy]>mat[i][j]+1: #+1이 없으면 이미 갱신된 셀을 또 갱신할 수 있으므로, 1보다 더 큰 셀 즉, 아직 갱신이 안된 무한대 값을 가진 셀을 찾기 위한 조건.
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
