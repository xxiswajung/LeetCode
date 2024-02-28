# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        Q=deque()
        Q.append(root)
        answer=[root.val]
        
        while Q:
            children=deque()
            while Q:
                item = Q.popleft()
                if item is not None:
                    if item.right is not None:
                        children.append(item.right)
                    if item.left is not None:
                        children.append(item.left)
            if children:
                answer.append(children[0].val)
            Q=children
        
        return answer
        