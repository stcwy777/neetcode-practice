class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1
        
        taskFreq = sorted(counter.values(), reverse=True)
        clock = 0
        for i, freq in enumerate(taskFreq):
            clock = max((freq - 1) * (n + 1) + i + 1, clock)

        return max(clock, len(tasks))