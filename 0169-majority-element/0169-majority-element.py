class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=Counter(nums)
        for x in dic:
            if dic[x]>len(nums)//2:
                return x