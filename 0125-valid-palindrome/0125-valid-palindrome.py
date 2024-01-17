class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.split(' ')
        res=''
        for x in s:
            x=x.lower()
            for i in range(len(x)):
                if x[i].isalnum():
                    res+=x[i]
        if res==res[::-1]:
            return True
        else:
            return False