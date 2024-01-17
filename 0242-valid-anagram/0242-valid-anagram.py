class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word=defaultdict(int)
        for i in s:
            word[i]+=1
        for j in t:
            word[j]-=1
        for x in word:
            if word[x]!=0:
                return False
        else:
            return True