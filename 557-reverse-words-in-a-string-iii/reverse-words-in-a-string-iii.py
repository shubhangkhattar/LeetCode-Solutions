class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        new_words = []
        for word in words:
            new_words.append(word[::-1])

        return " ".join(new_words)


