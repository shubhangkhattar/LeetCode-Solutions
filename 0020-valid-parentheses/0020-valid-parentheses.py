class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif len(stack) != 0:
                val = stack.pop()
                if (val == "(" and c == ")") or (val == "[" and c == "]") or (val == "{" and c == "}"):
                    continue
                else:
                    return False
            else:
                return False

        return True if len(stack) == 0 else False