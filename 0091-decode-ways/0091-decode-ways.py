class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp_array = {len(s) : 1}
        
        def dfs(index):
            if index in dp_array:
                return dp_array[index] 
            if s[index] == "0":
                return 0

            res = dfs(index + 1)

            if index+1 < len(s) and (s[index] == "1" or s[index] == "2" and s[index+1] in "0123456"):
                res += dfs(index+2)
            
            dp_array[index] = res

            return res

        return dfs(0)

