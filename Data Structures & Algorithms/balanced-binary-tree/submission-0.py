# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        hb=True
        def depth(root):
            nonlocal hb
            if not root:
                return 0
            left=depth(root.left)
            right=depth(root.right)
            
            if(left>right+1 or right>left+1):
                hb=False

            return 1+max(left,right)
        depth(root)
        return True if hb else False