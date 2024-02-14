class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            if len(heap)<k:
                heapq.heappush(heap,[-(x**2+y**2),[x,y]])
            else:
                heapq.heappushpop(heap,[-(x**2+y**2),[x,y]]) #가장 작은 것을 pop하고 item 을 push
                #거리를 음수로 표현하면 가장 작은 수가 곧 가장 먼 거리이므로 가장 작은 수를 pop 하는게 맞음
        return [coordinate for distance, coordinate in heap]