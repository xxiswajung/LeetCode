class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=''
        s=s.upper()
        for x in s:
            if x.isalpha() or x.isdecimal():
                ans+=x
        if ans==ans[::-1]:
            return True
        else:
            return False