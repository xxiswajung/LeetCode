class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph=defaultdict(list)
        n=len(bombs)
        
        for i in range(n):
            for j in range(n):
                if i!=j:
                    x1, y1, r1 = bombs[i]
                    x2, y2, _ = bombs[j]
                    if r1**2>=(x1-x2)**2+(y1-y2)**2:
                        graph[i].append(j)
        
        def DFS(cur, visited):
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    DFS(neighbor, visited)
            return len(visited)
        
        answer=0
        for i in range(n):
            visited=set()
            answer=max(answer,DFS(i,visited))
        return answer
                    