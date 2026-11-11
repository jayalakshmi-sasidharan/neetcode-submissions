# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(abs(left - right), self.res)

            return 1 + max(left, right)

        

        if root is None:
            return True
        else:
            dfs(root)
            if self.res > 1:
                return False
            else:
                return True
        