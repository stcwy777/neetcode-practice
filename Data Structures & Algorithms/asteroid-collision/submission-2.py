class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for ast in asteroids:
            alive = True
            if stack and stack[-1] > 0 and ast < 0:
                while stack and stack[-1] + ast < 0 and stack[-1] > 0:
                    stack.pop()

                if stack and stack[-1] + ast == 0:
                    stack.pop()
                    alive = False      
                elif stack and stack[-1] + ast > 0:
                    alive = False
                
            if alive:
                stack.append(ast)
        return stack