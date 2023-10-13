from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        visited = set()

        for course in prerequisites:
            pre_map[course[0]].append(course[1])

        def dfs(course):

            if not pre_map[course]:
                return True
            
            if course in visited:
                return False

            visited.add(course)

            for pre_course in pre_map[course]:
                if dfs(pre_course):
                    pre_map[course].remove(pre_course)
                else:
                    return False
            
            visited.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True



