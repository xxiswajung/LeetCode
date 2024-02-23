class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def DFS(v,tmp,chk):
            if v==len(nums):
                answer.append(tmp.copy())
                return
            for i in range(len(nums)):
                if chk[i]==0:
                    chk[i]=1
                    tmp.append(nums[i])
                    DFS(v+1,tmp,chk)
                    chk[i]=0
                    tmp.pop()
        answer=[]
        DFS(0,[],[0]*len(nums))
        return answer