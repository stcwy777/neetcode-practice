class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for [course, preq] in prerequisites:
            graph[preq].append(course)
        for node in graph.keys():
            q = deque(graph[node])
            visited = set({node})
            while q:
                for _ in range(len(q)):
                    x = q.pop()
                    if x == node:
                        return False
                    if x in graph and x not in visited:
                        q.extend(graph[x])
                        visited.add(x)
        
        return True
