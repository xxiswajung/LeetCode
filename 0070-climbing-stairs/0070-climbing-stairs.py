class Solution:
    def climbStairs(self, n: int) -> int:
        dy=[0]*(n+1)
        dy[1]=1
        if n==1 or n==2:
            return n
        else:
            dy[2]=2
            for i in range(3,n+1):
                dy[i]=dy[i-2]+dy[i-1]
            return dy[n]