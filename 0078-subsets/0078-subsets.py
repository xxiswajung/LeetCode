class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def DFS(v,check):
            if v==len(nums):
                pre=[]
                for i in range(len(check)):
                    if check[i]==1:
                        pre.append(nums[i])
                answer.append(pre)
                return
            check[v-1]=1
            DFS(v+1,check)
            check[v-1]=0
            DFS(v+1,check)
        
        answer=[]
        DFS(0,[0]*len(nums))
        return answer