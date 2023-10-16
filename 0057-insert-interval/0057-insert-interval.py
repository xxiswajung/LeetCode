class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        ans=[]
        i=0
        
        #1.newInterval의 왼쪽보다 작은 것들은 우선 pass
        while i<n and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i+=1
        #2.intervals들의 왼쪽과 newInterval의 오른쪽을 비교하여 overlapping할 부분을 체크해 newInterval 값 갱신
        #각각의 왼, 오를 비교하여 갱신
        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
        ans.append(newInterval)
        
        while i<n:
            ans.append(intervals[i])
            i+=1
        
        return ans