class Solution(object):
    def climbStairs(self, n):
        if n==1 or n==2:
            return n
        dp = [-1]*(n+1)
        dp[1],dp[2]=1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        
# class Solution(object):
#     def climbStairs(self,n):
#         def climb(n):
#             if n in memo:
#                 return memo[n]
#             else:
#                 memo[n]=climb(n-1)+climb(n-2)
#                 return memo[n]
#         memo = {1:1, 2:2} #use dictionary
#         return climb(n)