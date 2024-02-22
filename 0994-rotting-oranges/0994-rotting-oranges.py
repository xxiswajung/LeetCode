class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        xlen=len(grid)
        ylen=len(grid[0])
        minute=0
        visited=[[0]*ylen for _ in range(xlen)]
        Q=deque()

        for x in range(xlen):
            for y in range(ylen):
                if grid[x][y]==2:
                    Q.append((x,y,0))
        
        while Q:
            x,y,minute=Q.popleft()
            # result=max(minute,result)
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<xlen and 0<=yy<ylen and visited[xx][yy]==0 and grid[xx][yy]==1:
                    visited[xx][yy]=visited[x][y]+1
                    grid[xx][yy]=2
                    Q.append((xx,yy,minute+1))
                    
        for x in range(xlen):
            for y in range(ylen):
                if grid[x][y]==1:
                    return -1
        else:
            return minute