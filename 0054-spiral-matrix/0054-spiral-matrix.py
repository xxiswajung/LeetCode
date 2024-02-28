class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         answer=[]
        
#         while matrix:
#             answer+=matrix.pop(0)
            
#             if matrix and matrix[0]:
#                 for row in matrix:
#                     answer.append(row.pop())
            
#             if matrix:
#                 answer+=matrix.pop()[::-1]
            
#             if matrix and matrix[0]:
#                 for row in matrix[::-1]:
#                     answer.append(row.pop(0))
        
#         return answer
        dd=[(-1,0),(0,1),(1,0),(0,-1)]
        n,m=len(matrix),len(matrix[0])
        visited=[[0]*m for _ in range(n)]
        x,y,d=0,0,1
        visited[0][0]=1
        answer=[]
        answer.append(matrix[0][0])
        
        while True:
            if len(answer)==n*m:
                break
                
            xx=x+dd[d][0]
            yy=y+dd[d][1]

            if xx<0 or xx>=n or yy>=m or yy<0 or visited[xx][yy]==1:
                d=(d+1)%4
                continue
            
            answer.append(matrix[xx][yy])
            visited[xx][yy]=1
            x,y=xx,yy
        
        return answer
                    
        