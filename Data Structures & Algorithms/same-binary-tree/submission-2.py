# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            p1, p2 = stack.pop()
            if not p1 and not p2:
                continue
            if p1 and p2 and p1.val == p2.val:
                stack.append([p1.left, p2.left])
                stack.append([p1.right, p2.right])
            else:
                return False
        return True
        