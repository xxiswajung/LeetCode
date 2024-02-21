class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        xlen=len(grid)
        ylen=len(grid[0])
        visited=[[0]*ylen for _ in range(xlen)]
        
        def DFS(x,y):
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<xlen and 0<=yy<ylen and visited[xx][yy]==0 and grid[xx][yy]=="1":
                    visited[xx][yy]=1
                    DFS(xx,yy)
                    grid[xx][yy]="0"
        
        cnt=0
        for x in range(xlen):
            for y in range(ylen):
                if grid[x][y]=="1":
                    DFS(x,y)
                    cnt+=1
        return cnt