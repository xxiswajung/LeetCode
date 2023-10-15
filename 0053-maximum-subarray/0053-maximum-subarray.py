class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         ans = nums[0]
#         summ = 0

#         for num in nums:
#             if summ<0:
#                 summ=0
#             summ+=num
#             ans = max(ans, summ)

#         return ans

        ans = -100000
        summ = 0
        
        for num in nums:
            summ = max(summ+num, num)
            ans = max(ans,summ)
        return ans