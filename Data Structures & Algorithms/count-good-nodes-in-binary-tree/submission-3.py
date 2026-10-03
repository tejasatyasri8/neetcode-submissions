# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # def dfs(node,maxval):
        #     if not node:
        #         return 0
        #         count=0
        #     res=1 if maxval<=node.val else 0
        #     maxval=max(maxval,node.val)
        #     res+=dfs(node.left,maxval)
        #     res+=dfs(node.right,maxval)
        #     return res
        # return dfs(root,root.val)
        res=0
        q=deque()
        q.append((root,-float('inf')))
        while q:
            node,maxval=q.popleft()
            
            if node:
                if node.val>=maxval:
                    res+=1
                    maxval=node.val
                q.append((node.left,maxval))
                q.append((node.right,maxval))
        return res













