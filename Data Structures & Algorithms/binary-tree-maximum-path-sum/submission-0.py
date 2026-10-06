# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum=-float('inf')
        def max_depth(node):
            nonlocal max_sum
            if not node:
                return 0
            left=max(0,max_depth(node.left))
            right=max(0,max_depth(node.right))
            current_path=left+node.val+right
            max_sum=max(max_sum,current_path)
            return node.val+max(left,right)
        max_depth(root)
        return max_sum
