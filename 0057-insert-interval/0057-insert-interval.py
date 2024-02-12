class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        n=len(intervals)
        answer=[]
        
        while i<n and intervals[i][1]<newInterval[0]:
            answer.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval=(min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1]))
            i+=1
        answer.append(newInterval)
        while i<n:
            answer.append(intervals[i])
            i+=1
        return answer
                         