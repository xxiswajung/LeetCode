class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        pre={i:set() for i in range(1,n+1)}
        nxt=defaultdict(set)
        
        for u,v in relations:
            # nxt: 선수과목을 이수 후, 들을 수 있는 과목을 value로 가짐
            nxt[u].add(v)
            # pre: 들어야 하는 과목의 선수과목을 value로 가짐
            pre[v].add(u)
            
        # Q: 선수과목 없이 첫 학기에 들을 수 있는 과목
        Q=deque([u for u in pre if not pre[u]])
        # n: 들어야 하는 과목 수를 Q에 담긴 과목 수만큼 제거, 과목을 다 듣는 것(n=0)이 목표 
        n-=len(Q)
        answer=0
        
        while Q:
            for _ in range(len(Q)):
                u=Q.popleft()
                #Q에 있던 과목을 이수하면, 들을 수 있는 과목 이수 가능
                for v in nxt[u]:
                    pre[v].remove(u)
                    #선수과목을 다 이수 했으면, n 하나 줄이고 다음 과목으로 넘어가기
                    if len(pre[v])==0:
                        Q.append(v)
                        n-=1
            #Q: 한번에 담기는 과목 = 한 학기에 전부 들어야 함
            answer+=1
        
        return answer if n==0 else -1