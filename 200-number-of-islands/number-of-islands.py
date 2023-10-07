class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[-1]*len(grid[0]) for i in range(len(grid))]
        ROWS, COLS = len(grid) , len(grid[0])
 
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or visited[r][c] == 1:
                return
            visited[r][c] = 1
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        ans = 0
        print()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and visited[r][c] == -1:
                    ans +=1
                    dfs(r,c)

        return ans
