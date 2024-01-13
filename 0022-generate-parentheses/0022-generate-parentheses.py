class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dy=[[] for _ in range(n+1)]
        dy[1]=["()"]
        for i in range(2,n+1):
            for j in dy[i-1]:
                for k in range(len(j)):
                    item=j[:k]+'()'+j[k:]
                    dy[i].append(item)
            dy[i]=set(dy[i])
        return dy[n]