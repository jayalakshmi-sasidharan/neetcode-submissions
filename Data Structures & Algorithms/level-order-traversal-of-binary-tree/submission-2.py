# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #iterative bfs

        if not root:
            return []
        lvlOrder = []
        queue = deque([root])
        while queue:
            level = len(queue)
            newList = []
            for _ in range(level):
                node = queue.popleft()
                newList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lvlOrder.append(newList)
        return lvlOrder


        