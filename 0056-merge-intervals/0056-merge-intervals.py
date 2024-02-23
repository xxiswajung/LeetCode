class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        answer=[intervals[0]]
        
        for s,e in intervals:
            if s<=answer[-1][1]:
                answer[-1]=[answer[-1][0],max(answer[-1][1],e)]
            else:
                answer.append([s,e])
        return answer