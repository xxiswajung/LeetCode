class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        pre={i:set() for i in range(1,n+1)}
        nxt=defaultdict(set)
        for u,v in relations:
            nxt[u].add(v)
            pre[v].add(u)
        Q=deque([u for u in pre if not pre[u]])
        n-=len(Q)
        answer=0
        
        while Q:
            for _ in range(len(Q)):
                u=Q.popleft()
                for v in nxt[u]:
                    pre[v].remove(u)
                    if len(pre[v])==0:
                        Q.append(v)
                        n-=1
            answer+=1
        
        return answer if n==0 else -1