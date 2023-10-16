class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        Q=deque()
        
        for i, row in enumerate(mat):
            for j, element in enumerate(row):
                if element:
                    mat[i][j] = float('inf')
                else:
                    Q.append((i,j))
        
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        
        while Q:
            for k in range(len(Q)):
                i, j = Q.popleft()
                for t in range(4):
                    xx=i+dx[t]
                    yy=j+dy[t]
                    if 0<=xx<m and 0<=yy<n and mat[xx][yy]>mat[i][j]+1:
                        mat[xx][yy]=mat[i][j]+1
                        Q.append((xx,yy))
        return mat
