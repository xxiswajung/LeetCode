"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return
        
#         clone = Node(node.val) #입력에는 첫번째 값인 노드 1만 복사
#         clones = {node: clone} #원본 입력값이 복제값을 가리키도록 / hash table 의 용도 : 같은 노드 중복 생성 방지
#         Q = deque([node])
        
#         while Q:
#             node = Q.popleft()
#             for x in node.neighbors:
#                 if x not in clones:
#                     clones[x]=Node(x.val) #이웃 노드 생성
#                     Q.append(x) 
#                 clones[node].neighbors.append(clones[x]) #복제된 노드에 복제된 이웃 노드 연결
#         return clone
        
        if not node:
            return
        
        clones={}
        
        def dfs(node):
            if node in clones: #이미 노드가 해시테이블에 있는경우
                return clones[node] #노드를 또 만들 필요 없음
            clone = Node(node.val) #새롭게 노드를 만들어야 하는 경우
            clones[node]=clone
            for x in node.neighbors:
                clone.neighbors.append(dfs(x))
            return clone
        return dfs(node)