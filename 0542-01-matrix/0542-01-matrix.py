class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        dis=[[0]*len(mat[0]) for _ in range(len(mat))]
        Q=deque()
        
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y]:
                    mat[x][y]=10000000
                else: #mat[x][y]==1 or 자연수
                    Q.append((x,y))
        
        while Q:
            x,y=Q.popleft()
            cnt=1
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<len(mat) and 0<=yy<len(mat[0]) and mat[xx][yy]>mat[x][y]+1:
                    mat[xx][yy]=mat[x][y]+1
                    Q.append((xx,yy))
        return mat