class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #using backtracking
        answer=[]
        
        def DFS(i, cur, total):
            if total==target:
                answer.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            cur.append(candidates[i])
            DFS(i,cur,total+candidates[i])
            cur.pop() #마지막에 추가한 숫자를 제거: 재귀로 인해 발생한 상태 변경을 되돌리기 위해=앞줄에서 +candidate[i]를 했으니, 지금은 -candidate[i]해서 원상복귀
            DFS(i+1,cur,total) #가능한 모든 조합 탐색
        
        DFS(0,[],0)
        return answer