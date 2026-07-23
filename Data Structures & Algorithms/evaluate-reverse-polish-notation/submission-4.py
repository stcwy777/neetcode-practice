class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '*', '/'])
        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()

                if t == '+':
                    stack.append(int(left + right))
                elif t == '-':
                    stack.append(int(left - right))
                elif t == '*':
                    stack.append(int(left * right))
                else:
                    stack.append(int(left / right))
        return int(stack.pop())