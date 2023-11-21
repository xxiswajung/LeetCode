class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ch=[0]*(max(nums)+1)
        res=[]
        ans=[]
        def DFS(v):
            if v==len(nums):
                ans.append(res.copy())
                return
            else:
                ch[nums[v]]=1
                res.append(nums[v])
                DFS(v+1)
                ch[nums[v]]=0
                res.pop()
                DFS(v+1)
        DFS(0)
        return ans