class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_=Counter(nums)
        for x in nums:
            if nums_[x]>(len(nums)//2):
                return x