# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        minBad=2**31
        s,e=1,n
        while s<=e:
            mid=(s+e)//2
            print(mid)
            if isBadVersion(mid) is False:
                s=mid+1
            else:
                minBad=min(minBad,mid)
                e=mid-1
        return minBad