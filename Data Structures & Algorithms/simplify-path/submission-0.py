class Solution:
    def simplifyPath(self, path: str) -> str:
        comps = path.split('/')

        stack = []

        for comp in comps:
            if comp == '' or comp == '.':
                continue
            elif comp == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(comp)
        
        return '/' + '/'.join(stack)
            