# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_):
            if not root:
                return 0
            count = 0
            if root.val >= max_:
                max_ = root.val
                count += 1
            left = dfs(root.left,max_)
            right = dfs(root.right, max_)
            return left + right + count
        return dfs(root,root.val)

        