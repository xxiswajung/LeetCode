class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        ans=0
        
        while start<end:
            less=min(height[start],height[end])
            amount=less*(end-start)
            ans = max(amount,ans)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        
        return ans