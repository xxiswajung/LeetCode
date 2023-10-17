class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chk=set()
        i=0
        j=1
        s=list(s)
        mx=0
        while i<len(s):
            res=s[i:j]
            for x in res:
                chk.add(x)
            if len(chk)==j-i:
                mx=max(mx,j-i)
                j+=1
            else:
                chk=set()
                i+=1
                j=i+1
        return mx