class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirc = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if ((r, c) in path or 
                r < 0 or c < 0 or r >= m or c >= n or
                board[r][c] != word[i] ):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for row in range(m):
            for col in range(n):
                if dfs(row, col, 0):
                    return True
        return False

        

        
        


                
                    