# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hashInOrder = {val:ind for ind, val in enumerate(inorder)}
        self.preInd = 0


        def dfs(left,right):
            if left > right:
                return None

            root = TreeNode(preorder[self.preInd])
            self.preInd += 1
            index = hashInOrder.get(root.val)

            root.left = dfs(left,index - 1)
            root.right = dfs(index+1,right)

            return root

        return dfs(0, len(inorder) - 1)






        
        