# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         hash={}
#         ans=[]
#         res=[]
#         for i in range(len(points)):
#             length=int(math.pow(points[i][0],2)+math.pow(points[i][1],2))
#             ans.append((i,length))
#         ans.sort(key=lambda x:x[1])
        
#         i=0
#         while k!=0:
#             res.append(points[ans[i][0]])
#             i+=1
#             k-=1
#         return res

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = -(x*x + y*y) #Max Heap : 부모 노드 값이 자식들 값 보다 큰 트리
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y)) #item을 heap에 push 하고, 가장 작은 값을 pop
                #현재 heap은 음수처리가 되어있으므로, 음수에서 가장 작은 값 = 양수에서 가장 큰 값
                #우리가 원하는건 양수에서 가장 작은 값을 원하므로 heap에 k개의 작은 값만 모으기 위해 큰값들을 전부 pop해야함
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]
