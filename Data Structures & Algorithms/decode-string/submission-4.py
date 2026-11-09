class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        cur_str = ""
        cur_num = 0
        stack = []
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                stack.append((cur_str, cur_num))
                cur_num = 0
                cur_str = ''

            elif c == ']':
                prev_str, prev_num = stack.pop()
                cur_str = prev_str + prev_num * cur_str
            else:
                cur_str += c

        return cur_str