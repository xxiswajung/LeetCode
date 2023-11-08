class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        global answer
        answer = 0
        m=len(grid)
        n=len(grid[0])
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        minute = [[0]*n for _ in range(m)]
        Q=deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    Q.append((i,j))
        
        while Q:
            x,y=Q.popleft()
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<m and 0<=yy<n and grid[xx][yy]==1:
                    grid[xx][yy]=2
                    minute[xx][yy]=minute[x][y]+1
                    Q.append((xx,yy))
        
        flag=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    flag=0
        
        if flag==1:
            for i in range(m):
                for j in range(n):
                    if minute[i][j]>answer:
                        answer=minute[i][j]
            return answer
        else:
            return -1
