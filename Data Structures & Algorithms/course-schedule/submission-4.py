class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        # Build adjacent list
        for course, preq in prerequisites:
            graph[preq].append(course)
        
        # dfs
        def dfs(node: int, status: List[int]) -> bool:
            if len(graph[node]) == 0:
                return True
            if status[node] == 0:
                status[node] = 1
                for to_node in graph[node]:
                    if not dfs(to_node, status):
                        return False
            else:
                return False
            
            return True
        
        for node in graph.keys():
            tracker = [0] * numCourses
            if not dfs(node, tracker):
                return False
        return True

            