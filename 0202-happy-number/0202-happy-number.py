class Solution:
    def isHappy(self, n: int) -> bool:
        rec=[n]
        while True:
            sum=0
            for c in str(n):
                sum+=int(c)**2
            n=sum
            if n==1 or n in rec:
                break
            rec.append(sum)
        return True if n==1 else False