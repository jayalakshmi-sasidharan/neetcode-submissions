# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxSoFar): 
            if root and root.val >= maxSoFar:
                maxSoFar = root.val
                self.res += 1
            if root and root.left:  
                dfs(root.left,maxSoFar)
            if root and root.right:
                dfs(root.right,maxSoFar)

        self.res = 1
        self.maxSoFar = root.val
        dfs(root.left, self.maxSoFar)
        dfs(root.right, self.maxSoFar)

        return self.res


        