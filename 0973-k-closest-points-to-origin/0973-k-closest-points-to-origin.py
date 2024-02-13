class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            if len(heap)<k:
                heapq.heappush(heap,[-(x**2+y**2),[x,y]])
            else:
                heapq.heappushpop(heap,[-(x**2+y**2),[x,y]])
        return [pair for value, pair in heap]