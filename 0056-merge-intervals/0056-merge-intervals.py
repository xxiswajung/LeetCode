class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        answer=[intervals[0]]
        
        for i in range(1,len(intervals)):
            if intervals[i][0]<=answer[-1][1]:
                answer[-1]=[answer[-1][0],max(answer[-1][1],intervals[i][1])]
            else:
                answer.append(intervals[i])
        
        return answer