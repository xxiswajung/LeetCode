class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        semi=[]
        for i in range(len(nums)-1):
            for j in range(len(nums)-1,i,-1):
                if nums[i]>nums[j]:
                    semi.append((i,(j-i+1)))
                    break
        semi.sort(key=lambda x:x[1], reverse=True)
        if semi:
            return semi[0][1]
        else:   
            return 0