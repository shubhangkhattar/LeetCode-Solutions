class Solution:

    def dfs(self, i, j, grid, visited):
        if grid[i][j] != "1" or visited[i][j] == "1":
            return

        visited[i][j] = "1"

        if i+1 < len(grid):
            self.dfs(i+1,j,grid,visited)
        if i-1 >= 0:
            self.dfs(i - 1, j, grid, visited)
        if j + 1 < len(grid[0]):
            self.dfs(i, j+1, grid, visited)
        if j - 1 >= 0:
            self.dfs(i, j-1, grid, visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [["0"]*len(grid[0]) for i in grid]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1") and (visited[i][j] == "0"):
                    count += 1
                    self.dfs(i,j,grid,visited)

        return count