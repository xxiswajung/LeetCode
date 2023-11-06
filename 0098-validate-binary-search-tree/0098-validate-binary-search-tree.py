# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.Valid(root, float("-inf"), float("inf"))
    def Valid(self, root, left, right) -> bool:
        if not root:
            return True
        if not (root.val < right and root.val > left):
            return False
        return self.Valid(root.left, left, root.val) and self.Valid(root.right, root.val, right)
        # left subtree : 부모트리보다 작으므로 오른쪽 boundary 갱신 -> right = root.val
        # right subtree : 부모트리보다 크므로 왼쪽 boundary 갱신 -> left = root.val
        