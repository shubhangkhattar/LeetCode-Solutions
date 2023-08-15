from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        taken = set()

        for course, p in prerequisites:
            pre[course].append(p)

        def dfs(course):
            if not pre[course]:
                return True

            if course in taken:
                return False

            taken.add(course)

            for p in pre[course]:
                if not dfs(p):
                    return False

            pre[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

