class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        nums.sort()
        
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total==0:
                    answer.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return answer
        
            
            