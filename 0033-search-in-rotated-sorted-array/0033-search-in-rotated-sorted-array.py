class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)
        if length<1:
            return -1
        
        def BST(left,right,nums,target):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    return mid
                else:
                    if nums[left]<=nums[mid]:
                        if nums[left]<=target and target<nums[mid]:
                            right=mid-1
                        else:
                            left=mid+1
                    else:
                        if nums[mid]<target and target<=nums[right]:
                            left=mid+1
                        else:
                            right=mid-1
            return -1
        
        return BST(0,length-1,nums,target)
        
        
                    