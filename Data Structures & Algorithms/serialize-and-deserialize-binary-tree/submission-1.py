# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root:
            return "N"
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(",")
        self.i = 0
        if val[self.i] == "N":
            return None
        root = TreeNode(int(val[self.i]))
        queue = deque([root])
        self.i += 1

        while queue:
            node = queue.popleft()
            if val[self.i] != "N":
                node.left = TreeNode(int(val[self.i]))
                queue.append(node.left)
            
            self.i += 1
            if val[self.i] != "N":
                node.right = TreeNode(int(val[self.i]))
                queue.append(node.right)
            
            self.i += 1
        
        return root
        
            
            
            
        

