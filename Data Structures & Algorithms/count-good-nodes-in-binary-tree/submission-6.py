# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, float('-inf')))
        res = 0
        while queue:
            node, maxVal = queue.popleft()
            if node.val >= maxVal:
                maxVal = node.val
                res += 1
            if node.left:
                queue.append((node.left, maxVal))
            if node.right:
                queue.append((node.right, maxVal))
        
        return res


        