class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        m=len(board)
        n=len(board[0])
        
        def DFS(x,y,idx):
            global cmp, flag
            if idx==len(word):
                return True
            else:
                for i in range(4):
                    xx=x+dx[i]
                    yy=y+dy[i]
                    if idx<len(word) and 0<=xx<m and 0<=yy<n and visited[xx][yy]==0 and board[xx][yy]==word[idx]:
                        visited[xx][yy]=1
                        cmp+=board[xx][yy]
                        if DFS(xx,yy,idx+1):
                            return True
                        visited[xx][yy]=0
                        cmp=cmp[:-1]
        global cmp
        cmp=''
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited=[[0]*n for _ in range(m)]
                    visited[i][j]=1
                    cmp+=board[i][j]
                    if DFS(i,j,1):
                        return True
                    cmp=''
        return False
        