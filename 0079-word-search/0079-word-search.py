class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board[0])
        n=len(board)
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        
        def DFS(v,x,y):
            if v==len(word):
                return True
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<n and 0<=yy<m and visited[xx][yy]==0 and board[xx][yy]==word[v]:
                    visited[xx][yy]=1
                    if DFS(v+1,xx,yy):
                        return True
                    visited[xx][yy]=0
        
        for x in range(n):
            for y in range(m):
                if board[x][y]==word[0]:
                    visited = [[0]*m for _ in range(n)]
                    visited[x][y]=1
                    if DFS(1,x,y):
                        return True
        else:
            return False