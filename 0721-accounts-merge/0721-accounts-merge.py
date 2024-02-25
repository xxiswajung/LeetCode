class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited=[0]*len(accounts)
        address=defaultdict(list)
        answer=[]
        
        #i: index(=person), account(=name, email)
        for i, account in enumerate(accounts):
            for j in range(1,len(account)):
                email = account[j]
                address[email].append(i)
        
        def DFS(i, emails):
            if visited[i]==1:
                return
            visited[i]=1
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                emails.add(email)
                for neighbor in address[email]:
                    DFS(neighbor, emails)
        
        for i, account in enumerate(accounts):
            if visited[i]==1:
                continue
            name, emails=account[0],set()
            DFS(i,emails)
            answer.append([name]+sorted(emails))
        
        return answer