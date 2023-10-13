class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights),len(heights[0])

        pac, atl = set(),set()

        def dfs(r,c,ocean,prev):
            if (r,c) in ocean or r == ROWS or c == COLS or r < 0 or c < 0 or heights[r][c] < prev:
                return
                    
            ocean.add((r,c))
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r-1,c,ocean,heights[r][c])
            dfs(r,c+1,ocean,heights[r][c])
            dfs(r,c-1,ocean,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,0, pac, heights[r][0])
            dfs(r,COLS-1, atl, heights[r][COLS-1])
            
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res


