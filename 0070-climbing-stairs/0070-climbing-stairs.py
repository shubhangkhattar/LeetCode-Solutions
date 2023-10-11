class Solution:
    def climbStairs(self, n: int) -> int:
        
        hashmap = {}

        def dfs(stair):
            if stair > n:
                return 0
            elif stair == n:
                return 1
            
            if stair in hashmap:
                return hashmap[stair]
            
            ways = dfs(stair+1) + dfs(stair+2)
            hashmap[stair] = ways

            return ways

        return dfs(0)