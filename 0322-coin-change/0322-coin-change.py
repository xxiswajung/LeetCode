class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dy=[999999]*(amount+1)
        dy[0]=0
        if min(coins)>amount and amount!=0:
            return -1
        for x in coins:
            for y in range(1,len(dy)):
                if y>=x:
                    dy[y]=min(dy[y],dy[y-x]+1)
        if dy[amount]==999999:
            return -1
        else:
            return dy[amount]