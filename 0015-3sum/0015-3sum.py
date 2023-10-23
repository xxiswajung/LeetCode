class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        
        for i in range(len(nums)-2):
            j,k=i+1,len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum>0:
                    k-=1
                elif sum<0:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    #중복제거, nums[i]와 nums[j]는 이미 정답에 넣었으니 같은 값들을 pass
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    #중복제거 후 새로운 값 비교를 위한 값 갱신
                    j+=1
                    k-=1
        return ans
                