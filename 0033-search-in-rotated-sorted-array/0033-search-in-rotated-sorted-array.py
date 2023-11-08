class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)
        if length<1:
            return -1
        
        def BST(left, right, nums, target):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    return mid
                #mid를 기준으로 왼편이 정렬된 배열
                if nums[left]<=nums[mid]:
                    #target이 왼편에 있을 때
                    if nums[left]<=target and target<nums[mid]:
                        right=mid-1
                    #target이 왼편에 없을 때
                    else:
                        left=mid+1
                #mid를 기준으로 오른편이 정렬된 배열
                else:
                    #target이 오른편에 있을 때
                    if nums[mid]<target and target<=nums[right]:
                        left=mid+1
                    #target이 왼편에 있을 때 
                    else:
                        right=mid-1
            return -1
        
        return BST(0, length-1, nums, target)
    
        
        
                    