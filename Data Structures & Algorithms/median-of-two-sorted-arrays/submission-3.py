class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        S, L = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)

        m, n = len(S), len(L)

        target = (m + n + 1) // 2

        l, r = 0, m

        while l <= r:
            cut = (l + r) // 2
            
            leftS = S[cut - 1] if cut > 0 else float('-inf')
            rightS = S[cut] if cut < m else float('inf')

            leftL = L[target - cut - 1] if (target - cut) > 0 else float('-inf')
            rightL = L[target - cut] if (target - cut) < n else float('inf')

            if leftS <= rightL and leftL <= rightS:
                if (m + n) % 2 == 0:
                    return (max(leftS, leftL) + min(rightS, rightL)) / 2.0
                
                else:
                    return max(leftS, leftL)
            
            elif leftS > rightL:
                r -= 1
            elif leftL > rightS:
                l += 1