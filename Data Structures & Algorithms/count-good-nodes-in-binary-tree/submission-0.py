# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxval = -9999999
        

        def dfs (node, maxval):
            if not node:
                return 0
            
            if node.val >= maxval:
                good = 1
            else: 
                good = 0
            
            newmax = max(maxval,node.val)

            left_good = dfs(node.left,newmax)
            right_good = dfs(node.right,newmax)

            return good+ right_good + left_good

        
        if not root:
            return 0


        return dfs(root,root.val)
            

