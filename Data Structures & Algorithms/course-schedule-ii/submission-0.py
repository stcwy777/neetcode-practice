class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        
        for crs, pre in prerequisites:
            graph[pre].append(crs)
        
        visited = set()
        path = []
        order = []
        def dfs(node: int) -> bool:
     
            if node in path:
                return True
            
            if node in visited:
                return False
            
            path.append(node)
            visited.add(node)

            for nei in graph[node]:
                if dfs(nei):
                    return True
            
            path.pop()
            order.append(node)
            
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return []
        return order[::-1]