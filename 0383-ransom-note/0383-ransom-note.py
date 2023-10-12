class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # hash={}
        # for i in range(97,123):
        #     hash[i]=0
        # for x in magazine:
        #     hash[ord(x)]+=1
        # for y in ransomNote:
        #     hash[ord(y)]-=1
        # for i in range(97,123):
        #     if hash[i]<0:
        #         return False
        # else:
        #     return True
        rans, maga = Counter(ransomNote), Counter(magazine)
        if rans & maga == rans:
            return True
        else:
            return False