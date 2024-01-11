class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        i=0
        j=1
        while i<j:
            if j==len(nums):
                i+=1
                j=i+1
            else:  
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
                    break
                else:
                    j+=1
        return res
                