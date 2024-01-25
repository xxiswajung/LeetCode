class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited=[[0]*len(image[0]) for _ in range(len(image))]
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]

        def DFS(x,y):
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<len(image) and 0<=yy<len(image[0]) and visited[xx][yy]==0 and image[xx][yy]==image[sr][sc]:
                    visited[xx][yy]=1
                    DFS(xx,yy)
                    
        visited[sr][sc]=1
        DFS(sr,sc)
        
        for x in range(len(image)):
            for y in range(len(image[0])):
                if visited[x][y]==1:
                    image[x][y]=color
        return image