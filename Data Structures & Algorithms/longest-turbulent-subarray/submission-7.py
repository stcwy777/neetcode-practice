class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0

        for i in range(1, len(arr)):
            if arr[i] == arr[0]:
                L += 1
            else:
                break
        if L == (len(arr) - 1):
            return 1
        elif L == (len(arr) - 2):
            return 2
        
        if arr[L + 1] > arr[L]:
            gt = False
        else:
            gt = True

        max_len = 2
        for R in range(L + 2, len(arr)):
            comp = arr[R] > arr[R-1] if gt else arr[R] < arr[R-1]
            if comp:
                gt = not gt
                max_len = max(max_len, R - L + 1)
            else:                
                L = R - 1
                if arr[L] == arr[R]:
                    L = R
                gt = not arr[R] > arr[L]

        return max_len                