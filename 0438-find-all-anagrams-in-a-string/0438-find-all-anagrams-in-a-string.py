class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        word=Counter(p)
        n=len(p)
        answer=[]

        for i in range(len(s)):
            for x in word:
                if s[i:i+n].count(x)!=word[x]:
                    break
            else:
                answer.append(i)
        
        return answer