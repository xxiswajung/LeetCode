class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = Counter(s)
        answer = 0
        odd = 0 
        
        for x in letter:
            if letter[x]%2==0:
                answer+=letter[x]
            else:
                odd=max(odd,letter[x])
                answer+=letter[x]-1
        if odd!=0:
            return answer+1
        else:
            return answer