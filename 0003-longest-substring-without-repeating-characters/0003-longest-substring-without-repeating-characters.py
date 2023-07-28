class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        front = 0
        back = 0

        current_set = set()

        max_length = 0

        while front < len(s):
            if s[front] not in current_set:
                current_set.add(s[front])
                max_length = max(len(current_set),max_length)
                front += 1
            else:
                current_set.remove(s[back])
                back += 1

        return max_length


if __name__ == "__main__":
    str = "pwwkew"

    print("The length of the longest substring without repeating characters is", Solution().lengthOfLongestSubstring(str))
