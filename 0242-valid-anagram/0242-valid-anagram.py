class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=dict()
        s=list(s)
        t=list(t)
        for i in range(97,123):
            d[i]=0
        for x in s:
            d[ord(x)]+=1
        for y in t:
            d[ord(y)]-=1
        for i in range(97,123):
            if d[i]!=0:
                return False
        else:
            return True