class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = [c.lower() for c in s if c.isalnum()]

        return sentence == sentence[::-1]