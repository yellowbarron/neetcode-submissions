class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        path=[]

        def backtracking (open,close):
            if open == n and close == n:
                res.append(''.join(path))
                
            
            #base 1 add (
            if open < n:
                path.append('(')
                backtracking(open+1,close)
                path.pop()

            if close < open: 
                path.append(')')
                backtracking(open,close+1)
                path.pop()
            
        
        backtracking(0,0)

        if n ==0:
            return []
        return res

        