class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            small_idx=i
            for j in range(i+1,len(nums)):
                if nums[small_idx]>nums[j]:
                    small_idx=j
            nums[small_idx],nums[i]=nums[i],nums[small_idx]
        return nums
        