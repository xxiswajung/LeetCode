class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        rooms=[]
        
        for start, end in intervals:
            #가장 일찍 끝난 회의의 종료 시간 <= 다음 회의의 시작 시간 : 회의실 재사용 가능
            #가장 일찍 끝난 회의의 종료 시간 > 다음 회의의 시작 시간 : 회의실 추가
            if rooms and rooms[0]<=start:
                heappop(rooms)
            heappush(rooms, end)
        return len(rooms)