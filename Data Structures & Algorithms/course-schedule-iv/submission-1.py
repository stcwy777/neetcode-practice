class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        visit = [[False] * numCourses for _ in range(numCourses)]

        for pre, crs in prerequisites:
            visit[pre][crs] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    visit[i][j] |= visit[i][k] and visit[k][j]
        
        rslts = []
        for pre, crs in queries:
            rslts.append(visit[pre][crs])
        
        return rslts