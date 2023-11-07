class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        m=len(grid)
        n=len(grid[0])
        visit=[['0']*n for _ in range(m)]

        def DFS(x,y):
            global cnt
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<m and 0<=yy<n and visit[xx][yy]=='0' and grid[xx][yy]=='1':
                    visit[xx][yy]=cnt
                    grid[xx][yy]='0'
                    DFS(xx,yy)
                    
            
        
        global cnt
        cnt=1
        for x in range(m):
            for y in range(n):
                if grid[x][y]=='1':
                    visit[x][y]=cnt
                    grid[x][y]='0'
                    DFS(x,y)
                    cnt+=1
        return cnt-1
            