class Solution:
    def decodeString(self, s: str) -> str:
        
        cur_num = 0
        cur_str = ''
        stack = []

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                stack.append((cur_num, cur_str))
                cur_num = 0
                cur_str = ''

            elif c == ']':
                prev_num, pre_str = stack.pop()
                cur_str = pre_str + prev_num * cur_str
                cur_num = 0
            else:
                cur_str += c

        return cur_str