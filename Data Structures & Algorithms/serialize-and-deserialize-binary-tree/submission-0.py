# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string=""
        def dfs(node):
            nonlocal string
            if not node:
                string+="N,"
                return

            string+=str(node.val)
            string+=','            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return string

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")[:-1]
        index=0
        
        def dfs():
            nonlocal index
            value=values[index]
            index+=1
            if value == "N":
                
                return None
            node=TreeNode(int(value))
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()



