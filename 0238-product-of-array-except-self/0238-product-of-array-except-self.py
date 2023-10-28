class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1]*len(nums)
        temp=1
        
        #자신의 왼쪽에 있는 수 곱하기
        for i in range(len(nums)):
            answer[i]*=temp
            temp*=nums[i]
        temp=1
        #자신의 오른쪽에 있는 수 곱하기
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=temp
            temp*=nums[i]
        return answer