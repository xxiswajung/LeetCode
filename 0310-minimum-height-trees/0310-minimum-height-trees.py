class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:  
        #Topological Sort
        
        if n<=2:
            return [i for i in range(n)]
        
        neighbors = [set() for i in range(n)]
        for s, e in edges:
            neighbors[s].add(e)
            neighbors[e].add(s)
        
        #leaves : do not have child leaf
        leaves=[]
        for i in range(n):
            if len(neighbors[i])==1:
                leaves.append(i)
                
        remaining_nodes=n
        while remaining_nodes>2:
            remaining_nodes-=len(leaves)
            new_leaves=[]
            while leaves:
                leaf=leaves.pop() #remove the vertex
                neighbor=neighbors[leaf].pop() #remove the edge each other
                neighbors[neighbor].remove(leaf) #remove the edge each other
                if len(neighbors[neighbor])==1: #another leaves appears
                    new_leaves.append(neighbor)
            leaves=new_leaves
        return leaves