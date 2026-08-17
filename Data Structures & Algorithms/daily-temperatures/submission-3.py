class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        rslt = [0] * len(temperatures)
        for idx, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                prev_t, prev_idx = stack.pop()
                rslt[prev_idx] = idx - prev_idx
            stack.append((t, idx))
        
        return rslt
            
