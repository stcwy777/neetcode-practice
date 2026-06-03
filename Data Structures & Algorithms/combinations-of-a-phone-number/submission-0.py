class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dials = {
            '1': '', '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
            '9': 'wxyz'
        }
        rslt = []
        n = len(digits)

        def helper(i: int, comb: str) -> None:
            if i == n:
                if comb != '':
                    rslt.append(comb)
            else:
                for s in dials[digits[i]]:
                    new_comb = comb + s
                    helper(i + 1, new_comb)
            return
        helper(0, '')
        return rslt