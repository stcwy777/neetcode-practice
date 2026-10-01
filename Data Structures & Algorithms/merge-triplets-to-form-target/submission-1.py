class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        
        for x, y, z in triplets:
            # 只要有一个位置超过 target，整个 triplet 都不能用
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            
            # 记录这个合法 triplet 能提供哪些目标值
            if x == target[0]:
                found[0] = True
            if y == target[1]:
                found[1] = True
            if z == target[2]:
                found[2] = True
        
        return all(found)