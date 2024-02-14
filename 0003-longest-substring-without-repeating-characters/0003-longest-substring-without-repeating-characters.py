class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end= 0, 1
        answer=0
       
        while end<=len(s):
            chk=s[start:end]
            if len(chk) == len(set(chk)):
                answer=max(answer,len(chk))
                end+=1
            else:
                start+=1
                end=start+1
        return answer