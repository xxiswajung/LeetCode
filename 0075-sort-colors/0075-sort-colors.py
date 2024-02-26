class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1
        #red : start, white : mid, blue : end
        
        while white<=blue:
            cur=nums[white]
            if cur==0:
                nums[white], nums[red]= nums[red], nums[white]
                red+=1
                white+=1
            elif cur==1:
                white+=1
            else:
                nums[white], nums[blue]=nums[blue], nums[white]
                blue-=1
                