class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area=inf
        points_table=set()
        
        for x, y in points:
            points_table.add((x,y))
            
        for x1, y1 in points:
            for x2, y2 in points:
                if x1>x2 and y1>y2: #양 대각선 점 찾는거임
                    if (x1,y2) in points_table and (x2,y1) in points_table:
                        min_area=min((x1-x2)*(y1-y2),min_area)
                  
        return 0 if min_area==inf else min_area