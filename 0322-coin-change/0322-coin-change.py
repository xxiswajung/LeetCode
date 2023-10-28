class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        init=100000
        dy=[init]*(amount+1)
        dy[0]=0
        for i in coins:
            for j in range(i,amount+1):
                dy[j]=min(dy[j],dy[j-i]+1)
        if dy[amount]==init:
            return -1
        return dy[amount]