class Solution:
    def isPalindrome(self, s: str) -> bool:

        def valid(s: str) -> bool:
            if ('A' <= s <= 'Z') or ('a' <= s <= 'z') or ('0' <= s <= '9'):
                return True
            else:
                return False

        L, R = 0, len(s) - 1
        s = s.lower()
        while L <= R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                if valid(s[L]) and valid(s[R]):
                    return False
                    
                if not valid(s[L]):
                    L += 1
                if not valid(s[R]):
                    R -= 1
        
        return True
                