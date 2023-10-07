from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = defaultdict(list)
        visited = set()

        for course,p in prerequisites:
            preMap[course].append(p)

        def dfs(course):

            if not preMap[course]:
                return True

            if course in visited:
                return False

            visited.add(course)

            for p in preMap[course]:
                if not dfs(p):
                    return False

            preMap[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
