class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def DFS(x,y,aa):
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<len(image) and 0<=yy<len(image[0]) and image[xx][yy]==aa and visit[xx][yy]==0:
                    image[xx][yy]=color
                    visit[xx][yy]=1
                    DFS(xx,yy,aa)
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]            
        visit=[[0]*(len(image[0])) for _ in range(len(image))] 
        visit[sr][sc]=1
        DFS(sr,sc,image[sr][sc])
        image[sr][sc]=color
        return image