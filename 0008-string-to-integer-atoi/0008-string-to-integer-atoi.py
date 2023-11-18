class Solution:
    def myAtoi(self, s: str) -> int:
        ans=''
        number=['0','1','2','3','4','5','6','7','8','9']
        symbol=['++','--','+-','-+']
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        s=s.strip()
        if not s:
            return 0
        
        sign=1
        if s[0] in ['+','-']:
            if s[0]=='-':
                sign=-1
            s=s[1:]
        
        result=0
        for char in s:
            if not char.isdigit():
                break
            result=result*10+int(char)
        result=sign*result
        
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result