class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        S, L = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        m = len(S)
        n = len(L)

        target = (m + n + 1) // 2

        l, r = 0, m

        while l <= r:
            i = (r - l) // 2 + l
            j = target - i

            leftS = float('-inf') if i == 0 else S[i-1]
            rightS = float('inf') if i == m else S[i]

            leftL = float('-inf') if j == 0 else L[j-1]
            rightL = float('inf') if j == n else L[j]

            if leftS <= rightL and leftL <= rightS:
                if (m + n) % 2:
                    return max(leftS, leftL)
                else:
                    return (max(leftS, leftL) + min(rightS, rightL)) / 2.0
            if leftS > rightL:
                r = i - 1
            else:
                l = i + 1
