# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer=[]
        Q=deque()
        Q.append((root,0))
        cur = 0
        tmp = []
        if root is None:
            return answer
        while Q:
            item, lvl =Q.popleft()
            if item is None:
                continue
            if lvl==cur:
                tmp.append(item.val)
            else:
                answer.append(tmp)
                cur=lvl
                tmp=[]
                tmp.append(item.val)
            Q.append((item.left,lvl+1))
            Q.append((item.right,lvl+1))
        answer.append(tmp)
        return answer