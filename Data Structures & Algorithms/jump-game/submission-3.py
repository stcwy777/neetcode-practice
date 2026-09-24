class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        tar = len(nums) - 1
        visited = set()
        q = deque([(0, nums[0])])

        while q:
            for i in range(len(q)):
                pos, n = q.popleft()

                if (pos + n) >= tar:
                    return True
                else:
                    for j in range(1, n + 1):
                        if pos + j not in visited:
                            q.append((pos + j, nums[pos + j]))
                            visited.add(pos + j)
        
        return False

