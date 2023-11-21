class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        
        while matrix:
            #1.3시 방향 : 원래 순서 그대로 저장
            ans+=matrix.pop(0)

            #2.6시 방향 : 각 줄의 끝의 원소만 저장
            if matrix and matrix[0]: #matrix[0]을 넣어야 하는 이유: [[1],[2],[3],[4],[5],[6],[7],[8],[9]] 일때, row.pop()하면 껍데기[]만 남음=matrix[0] is False
                for row in matrix:
                    ans.append(row.pop())
            #3.9시 방향 : 맨 끝의 배열을 역순으로 저장
            if matrix:
                ans+=matrix.pop()[::-1]
            #4.12시 방향 : 각 줄을 거꾸로, 맨 앞의 원소만 저장
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        return ans