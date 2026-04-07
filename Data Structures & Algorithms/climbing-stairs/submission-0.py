class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 0:
            return 0
        steps = [0] * n
  
        for i in range(n):
            # steps[0] = 1
            # steps[1] = 2
            if i <= 1:
                steps[i] = i + 1
            else:
                steps[i] = steps[i-1] + steps[i-2]
        
        return steps[n-1]