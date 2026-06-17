import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        # 初始化邻接表
        adj = {i: [] for i in range(N)}
        for i in range(N):
            for j in range(i + 1, N):
                # 修复 1：正确计算 y 坐标的差值
                manDis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                # 优化：只需记录相邻节点和距离即可
                adj[i].append((manDis, j))
                adj[j].append((manDis, i))
        
        # 修复 2：visit 集合用来记录访问过的【节点】
        visit = set()
        heap = [(0, 0)]  # (distance, node)
        total_cost = 0   # 直接累加总代价
        
        while heap:
            # 如果所有节点都已经加入树中，提前结束
            if len(visit) == N:
                break
                
            dis, node = heapq.heappop(heap)
            
            # 如果该节点已经连入最小生成树，直接跳过
            if node in visit:
                continue
                
            # 将节点标记为已访问，并将边长加入总代价
            visit.add(node)
            total_cost += dis
            
            # 遍历邻居，将未访问过的邻居加入堆
            for nDis, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(heap, (nDis, nei))
                    
        return total_cost