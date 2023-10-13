class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid),len(grid[0])

        visited = [[-1] * len(grid[0]) for i in range(len(grid)) ]
        
        count = 0

        def dfs(r,c):
            if (r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] != "1"  or visited[r][c] == 1):
                return 
            visited[r][c] = 1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and visited[i][j] == -1:
                    count += 1
                    dfs(i,j)

        return count
