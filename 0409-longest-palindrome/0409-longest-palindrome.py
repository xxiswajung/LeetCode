class Solution:
    def longestPalindrome(self, s: str) -> int:
        s=list(s)
        txt=Counter(s)
        answer=0
        maxx=0
        for i in txt:
            if txt[i]%2==0:
                answer+=txt[i]
            else:
                maxx=max(maxx,txt[i])
                answer+=txt[i]-1
        if maxx!=0:
            return answer+1
        else:
            return answer