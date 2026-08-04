class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        window = {}
        for i in range(m):
            c = s2[i]
            window[c] = window.get(c, 0) + 1

        if window == need:
            return True

        for r in range(m, n):
            # 新字符进入
            c = s2[r]
            window[c] = window.get(c, 0) + 1

            # 老字符离开
            left = s2[r - m]
            window[left] -= 1

            if window[left] == 0:
                del window[left]

            if window == need:
                return True

        return False