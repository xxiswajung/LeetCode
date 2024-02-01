# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer=0
        
        def DFS(node):
            if not node:
                return 0
            left, right = DFS(node.left), DFS(node.right) #현재 탐색중인 노드를 기준으로 왼쪽/오른쪽 자식노드들의 diameter 기록
            self.answer=max(self.answer,left+right) #최대 diameter와 왼+오를 더한 값을 저장(diameter는 결국 어떤 중심노드를 거쳐 왼쪽과 오른쪽의 높이를 저장하는 것이므로)
            return 1+max(left,right)
        
        DFS(root)
        return self.answer