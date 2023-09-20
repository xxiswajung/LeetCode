class Solution(object):
    def isPalindrome(self, x):
        x=list(str(x))
        y=x[::-1]
        if x==y:
            return True
        else:
            return False
        