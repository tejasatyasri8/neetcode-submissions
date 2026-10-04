# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={}
        for i in range(len(inorder)):
            inorder_map[inorder[i]]=i
        def build(pres,pree,ins,ine):
            if pres>pree:
                return None
            val=preorder[pres]
            root=TreeNode(val)
            root_index=inorder_map[val]
            left_size=root_index-ins
            root.left=build(
                pres+1,
                pres+left_size,
                ins,
                root_index-1
            )
            root.right=build(
                pres+left_size+1,
                pree,
                root_index+1,
                ine
            )
            return root


        return build(0,len(preorder)-1,0,len(inorder)-1)
