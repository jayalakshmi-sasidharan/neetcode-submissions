# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSame(root,subRoot):
            return True
        if root:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        return False

        


    
    def isSame(self, node, child):
        if not node and not child:
            return True
        if not node or not child:
            return False
        if node.val != child.val:
            return False
        return (self.isSame(node.left, child.left) and self.isSame(node.right, child.right))