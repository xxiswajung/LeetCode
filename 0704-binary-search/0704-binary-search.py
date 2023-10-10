class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        flag=0
        while i<=j:
            mid = (i+j)//2
            if nums[mid]<target:
                i=mid+1
            elif nums[mid]>target:
                j=mid-1
            else:
                flag=1
                return mid
        if flag==0:
            return -1