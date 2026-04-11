class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        ind = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            ind[crs] += 1

        queue = deque()
        taken = set()

        for i in range(numCourses):
            if ind[i] == 0:
                queue.append(i)
                taken.add(i)

        while queue:
            for i in range(len(queue)):
                crs = queue.popleft()

                for dep in graph[crs]:
                    ind[dep] -= 1
                    if ind[dep] == 0 and dep not in taken:
                        queue.append(dep)
                        taken.add(dep)
        if len(taken) == numCourses:
            return True
        else:
            return False
