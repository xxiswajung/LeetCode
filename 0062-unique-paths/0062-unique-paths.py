class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dx=[1,0]
        dy=[0,1]
        visited=[[0]*n for _ in range(m)]
        
        for x in range(n):
            for y in range(m):
                visited[y][0]=1
                visited[0][x]=1
        
        for x in range(1,n):
            for y in range(1,m):
                visited[y][x]=visited[y-1][x]+visited[y][x-1]
        return visited[m-1][n-1]