# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0
        def dfs(root):
            if not root:
                return 0
            nonlocal max_d
            left = dfs(root.left)
            right = dfs(root.right)
            max_d = max(max_d,left+right)
            return (max(left,right) +1)
        dfs(root)
        return max_d