class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0 
        visit = set()
        dir = [(1,0),(0,1),(0,-1),(-1,0)]
        def dfs (r,c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0 or ((r,c) in visit):
                    return 0
            visit.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c)+ dfs(r,c+1) + dfs(r,c-1))

                
        m,n = len(grid), len(grid[0])
        

        for r in range(m):
            for c in range(n):
                area = max(area, dfs(r,c))

        
        return area

        