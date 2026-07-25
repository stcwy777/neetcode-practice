class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        rslt = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                rslt[idx] = i - idx
            
            stack.append(i)
        return rslt