class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
            
        n = len(num1)
        m = len(num2)
        
        res = [0] * (m + n)
        
        for i in range(n - 1, -1, -1):
            v1 = ord(num1[i]) - ord('0')            
            for j in range(m - 1, -1, -1):
                v2 = ord(num2[j]) - ord('0')
                
                res[i + j + 1] = v1 * v2 + res[i + j + 1]
                res[i + j] += res[i + j + 1] // 10
                res[i + j + 1] = res[i + j + 1] % 10
        
        start = 0
        while res[start] == 0:
            start += 1
        
        return ''.join(map(str, res[start:]))