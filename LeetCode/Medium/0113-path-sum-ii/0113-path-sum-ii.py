# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans = []
        def dfs(root,targetSum,path):
            if not root:
                return 0
            path.append(root.val)
            if not root.left and not root.right:
                if root.val == targetSum:
                    ans.append(path[:])
            targetSum -= root.val
        
            dfs(root.left,targetSum,path)
            dfs(root.right,targetSum,path)
            path.pop()
        
        dfs(root,targetSum,[])
        return ans
        