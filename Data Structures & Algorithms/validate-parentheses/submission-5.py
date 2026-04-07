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
                pop_elem = left_brackets.pop()
                if s[i] == ')' and pop_elem != '(':
                    return False
                elif s[i] == ']' and pop_elem != '[':
                    return False
                elif s[i] == '}' and pop_elem!= '{':
                    return False
        if len(left_brackets) > 0:
            return False
        return True