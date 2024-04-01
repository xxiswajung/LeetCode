class Solution:
    def maxArea(self, height: List[int]) -> int:
        s,e=0,len(height)-1
        result=0
        
        while s<=e and True:
            result = max(result,(e-s)*min(height[e],height[s]))
            
            if height[e]>height[s]:
                s+=1
            else:
                e-=1
                
        return result
            
                