class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        island = 0
        m, n = len(grid), len(grid[0])
        dir = [(1,0),(0,1),(0,-1),(-1,0)]
        def dfs (r,c):

            for rd, cd in dir:
                row, col = r +rd, c+ cd
                if row >= 0 and col >= 0 and row < m and col < n and grid[row][col] == "1" and ((row,col)not in visit):
                    visit.add((row,col))
                    dfs(row,col)
            
            return

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r,c) not in visit:
                    visit.add((r,c))
                    dfs(r,c)
                    island +=1


        return island 
        