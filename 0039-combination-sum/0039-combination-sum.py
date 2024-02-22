class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        
        def DFS(i,cur,total):
            if total==target:
                answer.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            cur.append(candidates[i])
            DFS(i,cur,total+candidates[i])
            cur.pop()
            DFS(i+1,cur,total)
            
        DFS(0,[],0)
        return answer
            
        