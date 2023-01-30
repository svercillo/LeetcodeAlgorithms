class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-2

        while l <= r:
            m = (l+r) // 2
            if arr[m] > arr[m+1]:
                r = m - 1
            else:
                l = m + 1

        return l

