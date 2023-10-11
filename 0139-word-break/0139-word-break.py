class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp_array = [False] * (len(s)+1)
        dp_array[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp_array[i] = dp_array[i+len(word)] 
                    if dp_array[i]:
                        break
        

        return dp_array[0]