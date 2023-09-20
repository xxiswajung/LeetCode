class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        dp=[[1]]
        for i in range(1,numRows):
            res=[1]
            for j in range(1,i): # in case of i==1, this loop will not executed
                val = dp[i-1][j-1]+dp[i-1][j]
                res.append(val)
            res.append(1)
            dp.append(res)
        return dp
        