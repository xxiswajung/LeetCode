class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        init=inf
        dy=[init]*(amount+1)
        dy[0]=0
        for x in coins:
            for y in range(x,len(dy)):
                dy[y]=min(dy[y],dy[y-x]+1)
        if dy[amount]==inf:
            return -1
        else:
            return dy[amount]