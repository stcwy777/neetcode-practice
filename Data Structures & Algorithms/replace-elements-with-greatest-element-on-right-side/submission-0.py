class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxV = -1
        rslt = []
        for i in range(len(arr) - 1, -1, -1):
            rslt.append(maxV)
            maxV = max(arr[i], maxV)
            
        return rslt[::-1]
