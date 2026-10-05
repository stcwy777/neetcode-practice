class Solution:
    def checkValidString(self, s: str) -> bool:
        min_op, max_op = 0, 0
        
        for i in range(len(s)):
            if s[i] == '(':
                min_op += 1
                max_op += 1
            elif s[i] == ')':
                min_op -= 1
                max_op -= 1
            else:
                max_op += 1
                min_op -= 1

            if max_op < 0:
                return False
            min_op = max(min_op, 0)

        return min_op == 0
