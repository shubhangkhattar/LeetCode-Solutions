class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]
        ans = ""

        for i in range(len(check)):
            for j in range(1,len(strs)):
                if i < len(strs[j]) and strs[j][i] == check[i]:
                    continue
                else:
                    return ans
            ans += check[i]
        return ans