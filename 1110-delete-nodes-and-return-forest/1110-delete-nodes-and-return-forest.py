# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        #1. Traverse and find -> 2. connection 끊기 -> 3. 분리된 트리 만들기(?)
        
        answer=[]
        
        def DFS(root):
            if root is None:
                return
            root.left=DFS(root.left)
            root.right=DFS(root.right)
            if root.val not in to_delete:
                return root
            if root.left:
                answer.append(root.left)
            if root.right:
                answer.append(root.right)
            return None
        
        root=DFS(root)
        if root:
            answer.append(root)
        return answer
        