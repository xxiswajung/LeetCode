class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for x in s:
            x=x.lower()
            if x.isalpha() or x.isdecimal():
                res+=x
        print(res)
        if res==res[::-1]:
            return True
        else:
            return False