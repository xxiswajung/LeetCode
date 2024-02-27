class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        else:
            nums=sorted(nums)
            mid=sum(nums)//2
            dy=[False]*(mid+1)
            dy[0]=True
            
            for x in nums:
                for i in range(mid,x-1,-1):
                    dy[i]=dy[i] or dy[i-x]
            return dy[mid]
        