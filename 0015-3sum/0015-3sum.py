class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []   
        nums.sort()
        #nums=[-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            # 정렬을 했는데도 현재 값과 이전 값이 같으면 볼 필요 없음, 0이 안됨
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    #중복 피하기 위해
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return ans