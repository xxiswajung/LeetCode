class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while True:
            if all(nums[i]<=nums[i+1] for i in range(len(nums)-1)):
                break
            p,q=0,1
            while q<len(nums):
                if nums[p]>nums[q]:
                    nums[p], nums[q] = nums[q], nums[p]
                p+=1
                q+=1