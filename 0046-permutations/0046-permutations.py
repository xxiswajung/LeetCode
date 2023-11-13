class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visit=[0]*len(nums)
        answer=[]
        
        
        def DFS(v,arr):
            if v==len(nums):
                answer.append(arr.copy())
                return
            else:
                for i in range(len(nums)):
                    if visit[i]==0:
                        visit[i]=1
                        arr.append(nums[i])
                        DFS(v+1,arr)
                        visit[i]=0
                        arr.pop()
                        
        DFS(0,[])  
        return answer