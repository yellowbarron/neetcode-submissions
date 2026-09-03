# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stk = collections.deque()
        ans = []
        if root:
            stk.append(root)

        while stk:
            level = len(stk)
            levels = []
            for _ in range(level):

                c = stk.popleft()
                if c.right:
                    stk.append(c.right)

                if c.left:
                    stk.append(c.left)
                
                levels.append(c.val)
            
            ans.append(levels)
        
        output =[]
        for item in ans:
            if item:
                output.append(item[0])
        
        return output

            