class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        for c in s:
            
            if c == ']':
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                # '['
                stack.pop()
                count = ''
                while stack and '0' <= stack[-1] <= '9':
                    count = stack.pop() + count
                stack.append(int(count) * tmp)
            else:
                stack.append(c)
        
        return ''.join(stack)
