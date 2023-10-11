class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp_matrix = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

        for i in range(1,len(dp_matrix)):
            for j in range(1,len(dp_matrix[0])):
                if text1[i-1] == text2[j-1]:
                    dp_matrix[i][j] = dp_matrix[i-1][j-1] + 1
                else:
                    dp_matrix[i][j] = max(dp_matrix[i-1][j],dp_matrix[i][j-1])


        return dp_matrix[-1][-1]