class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        for c in s:
            
            if c == ']':
                tmp = []
                while stack[-1] != '[':
                    tmp.append(stack.pop())
                # '['
                stack.pop()
                count = []
                while stack and stack[-1].isdigit():
                    count.append(stack.pop())

                num = int(''.join(reversed(count)))
                sub_str = ''.join( reversed(tmp) )
                stack.append(num * sub_str)
            else:
                stack.append(c)
        
        return ''.join(stack)
