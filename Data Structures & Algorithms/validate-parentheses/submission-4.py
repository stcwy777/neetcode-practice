class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        left_brackets = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                left_brackets.append(s[i])
            elif len(left_brackets) == 0:
                return False
            else:
                if s[i] == ')' and left_brackets.pop() != '(':
                    return False
                elif s[i] == ']' and left_brackets.pop() != '[':
                    return False
                elif s[i] == '}' and left_brackets.pop() != '{':
                    return False
        if len(left_brackets) > 0:
            return False
        return True