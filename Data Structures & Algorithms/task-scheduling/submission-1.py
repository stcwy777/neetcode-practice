from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(max_heap)
        clock = 0
        print(max_heap)
        while max_heap:
            cycle = n + 1
            task_done = 0
            temp = []

            while cycle and max_heap:
                cnt = -1 * heapq.heappop(max_heap)

                if cnt > 1:
                    temp.append(-(cnt - 1))
                task_done += 1
                cycle -= 1

            for t in temp:
                heapq.heappush(max_heap, t)
            if not max_heap:
                clock += task_done
            else:
                clock += (n + 1)
        
        return clock
