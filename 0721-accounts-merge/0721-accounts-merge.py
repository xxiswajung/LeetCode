class UnionFind:
    def __init__(self,n):
        # 각 노드의 부모를 나타내는 리스트, 처음에는 자기 자신으로 초기화
        self.par = [i for i in range(n)]
        # 각 트리의 높이를 나타내는 리스트
        self.rank = [1]*n
    
    def find(self,x):
        # 루트 노드를 찾을 때 까지 재귀적으로 탐색
        while x!=self.par[x]: #노드 x가 이미 루트라면 더이상의 재귀 호출을 하지 않음
            self.par[x] = self.par[self.par[x]]
            x=self.par[x]
        return x
    
    def union(self,x1,x2):
        # 각 노드의 루트 노드를 찾음
        p1,p2=self.find(x1), self.find(x2)
        # 두 트리의 높이(rank)를 비교하여, 낮은 트리를 높은 트리에 붙임
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} # maps email to index of accounts
        
        for i, a in enumerate(accounts): # i: index, a: name, email, email, ...
            for e in a[1:]: # a에서 name을 제외한 이메일들 중에서 
                if e in emailToAcc: # 이미 동일한 이메일이 emailToAcc에 있다면 => 동일인물의 것
                    uf.union(i,emailToAcc[e]) # 그 사람(i)에 이메일(emailToAcc[e]) 합치기
                else:
                    emailToAcc[e]=i # 딕셔너리에서 이메일을 key로, 사람이름이 아닌 사람index를 value로 설정하여 저장
        
        emailGroup = defaultdict(list) # maps index of accounts to list of emails
        for e, i in emailToAcc.items():
            leader = uf.find(i) # 계정 주인 찾기
            emailGroup[leader].append(e) # 계정주인에게 이메일 추가
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name]+sorted(emailGroup[i])) # array concat
        return res