class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rslt = []
        path = []

        def explore(left: int, right: int) -> None:

            if left > n or right > n or right > left:
                return
            
            elif left == right and left == n:
                rslt.append(''.join(path))
            
            path.append('(')
            explore(left + 1, right)
            path.pop()
            path.append(')')
            explore(left, right + 1)
            path.pop()
        
        explore(0, 0)

        return rslt