class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front = 0
        back = 0


        current_set = set()
        max_count = 0

        while front < len(s):

            if s[front] not in current_set:
                current_set.add(s[front])
                max_count = max(max_count,len(current_set))
                front += 1

            else:
                current_set.remove(s[back])
                back += 1


        return max_count