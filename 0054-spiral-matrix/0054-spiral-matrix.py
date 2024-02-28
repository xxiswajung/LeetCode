class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m=len(matrix[0])
        # n=len(matrix)
        # answer=[]
        # i=0
        # while len(answer)!=m*n:
        #     for p in range(i,m-i-1):
        #         answer.append(matrix[i][p])
        #     for q in range(i,n-i-1):
        #         answer.append(matrix[q][m-i-1])
        #     for p in range(m-i-1,i,-1):
        #         answer.append(matrix[n-i-1][p])
        #     for q in range(n-i-1,i,-1):
        #         answer.append(matrix[q][i])
        #     i+=1
        # return answer
        
        answer=[]
        
        while matrix:
            answer+=matrix.pop(0)
            
            if matrix and matrix[0]:
                for row in matrix:
                    answer.append(row.pop())
            
            if matrix:
                answer+=matrix.pop()[::-1]
            
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    answer.append(row.pop(0))
        
        return answer
        