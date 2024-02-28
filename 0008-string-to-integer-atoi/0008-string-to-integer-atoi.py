class Solution:
    def myAtoi(self, s: str) -> int:
        pos=1
        sign=False
        dig=False
        answer=''
        for x in s:
            if (sign is True or dig is True) and x.isdigit() is False:
                    break
            if x=='+':
                pos=1
                sign=True
            elif x=='-':
                pos=-1
                sign=True
            elif x.isdigit():
                answer+=x
                dig=True
            elif x==' ':
                continue
            else:
                break
        if answer=='':
            return 0
        else:
            ans=pos*int(answer)
            if ans<-math.pow(2,31):
                return -int(math.pow(2,31))
            elif ans>math.pow(2,31)-1:
                return int(math.pow(2,31)-1)
            else:
                return ans
            