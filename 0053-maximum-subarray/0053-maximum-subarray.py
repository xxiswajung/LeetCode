class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        summ = 0

        for num in nums:
            summ = max(num, summ + num)
            ans = max(ans, summ)

        return ans