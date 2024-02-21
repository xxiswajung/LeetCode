class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1]*(len(nums))
        tmp=1
        
        for i in range(len(nums)):
            answer[i]*=tmp
            tmp*=nums[i] #본인의 왼쪽 수
        tmp=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=tmp
            tmp*=nums[i]
        return answer