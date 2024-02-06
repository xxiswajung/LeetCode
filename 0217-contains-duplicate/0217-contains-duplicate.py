class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countable=Counter(nums)
        for x in countable:
            if countable[x]>1:
                return True
        else:
            return False