from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        elif k == len(nums):
            return [max(nums)]
        
        queue = deque(sorted(zip(nums[:k], range(k)), reverse=True))

        rslt = [queue[0][0]]
        for i in range(k, len(nums)):

            while queue[0][1] <= (i - k):
                queue.popleft()

            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))

            rslt.append(queue[0][0])
        return rslt

