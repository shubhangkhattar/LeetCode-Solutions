class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_array = [[0]*(len(text2)+1) for i in range((len(text1)+1))]
        for i in range(1, len(dp_array)):
            for j in range(1, len(dp_array[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp_array[i][j] = 1 + dp_array[i - 1][j - 1]
                else:
                    dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])

        return dp_array[-1][-1]